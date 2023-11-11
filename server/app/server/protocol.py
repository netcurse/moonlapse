import logging
from typing import Literal
import uuid
import trio
from sqlalchemy.orm import sessionmaker
from app.server.logging_adapter import ProtocolLoggerAdapter
import app.net as packets

MAX_PACKET_SIZE = 1024 * 5  # 5 KiB
READ_TIMEOUT = 10   # seconds

class Protocol:
    def __init__(self, server_stream: trio.SocketStream, core):
        self.server_stream = server_stream
        self.ident = uuid.uuid4()
        self.core = core
        self.SessionFactory: sessionmaker = core.SessionFactory

        from app.server import protostates
        self.protostate: protostates.ProtoState = protostates.EntryState(self)

        # set up the logger adapter with additional context
        self.logger = ProtocolLoggerAdapter(logging.getLogger(__name__), {
            'ident': self.ident,
            'protostate': self.protostate
        })

    async def start(self):
        try:
            while True:
                data = await self.read_message(self.server_stream)
                if data is None:
                    break  # connection closed by the client, timeout, or error
                await self.handle_message(data)
        except Exception as exc:
            self.logger.warning(f"crashed: {exc!r}")
        finally:
            self.logger.info(f"connection closed")

    async def read_message(self, stream):
        message_bytes = b''
        try:
            with trio.fail_after(READ_TIMEOUT):  # timeout
                length_bytes = await stream.receive_some(4)
                if not length_bytes:
                    return None

                message_length = int.from_bytes(length_bytes, byteorder='big')

                if message_length > MAX_PACKET_SIZE:
                    raise ValueError("Packet size too large")

                message_bytes = b''
                while len(message_bytes) < message_length:
                    chunk = await stream.receive_some(message_length - len(message_bytes))
                    if not chunk:
                        break
                    message_bytes += chunk

                if len(message_bytes) != message_length:
                    raise ValueError("Incomplete packet received")

                return message_bytes
        except (trio.TooSlowError):
            self.logger.warning(f"Timeout while reading message. Received {len(message_bytes)} bytes: {message_bytes}")
            return None
        except (ValueError) as exc:
            self.logger.warning(f"Error reading message: {exc}")
            return None
    
    async def send_packet(self, packet: packets.Packet):
        await self.send_message(packet.SerializeToString())
    
    async def send_message(self, message: bytes):
        length_prefix = len(message).to_bytes(4, byteorder='big')
        await self.server_stream.send_all(length_prefix + message)

    async def handle_message(self, data: bytes):
        try:
            packet = packets.Packet.FromString(data)
        except Exception as exc:
            self.logger.warning(f"received invalid packet: {exc!r}")
            return
        
        # dispatch
        if packet.HasField("login"):
            await self.protostate.handle_login_packet(packet.login)
        elif packet.HasField("register"):
            await self.protostate.handle_register_packet(packet.register)
        elif packet.HasField("chat"):
            await self.protostate.handle_chat_packet(packet.chat)
        elif packet.HasField("heartbeat"):
            self.logger.info(f"received heartbeat packet")
            # ignore heartbeat packets
            pass
        else:
            # otherwise, log warning and ignore
            self.logger.warning(f"received unknown packet {packet!r}")

    def set_state(self, state: Literal["Entry", "Play"]):
        from app.server import protostates

        protostate = getattr(protostates, f"{state}State")(self)    # kinda jank

        self.logger.info(f"changing protostate to {state}")
        self.protostate = protostate
        self.logger.extra['protostate'] = protostate