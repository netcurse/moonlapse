from abc import ABC, abstractmethod
from app.server.protocol import Protocol
from app.net import DenyPacket, Packet, create_deny_packet

class ProtoState(ABC):
    def __init__(self, protocol: Protocol):
        self.proto = protocol

    def __str__(self) -> str:
        return self.__class__.__name__

    async def log_unregistered_packet(self, packet):
        self.proto.logger.warning(f"received {packet.DESCRIPTOR.name} packet in unregistered state")
        p = create_deny_packet("You cannot send that packet in this state")  # todo: better error message
        await self.proto.send_packet(p)
    
    async def handle_login_packet(self, packet):
        await self.log_unregistered_packet(packet)

    async def handle_register_packet(self, packet):
        await self.log_unregistered_packet(packet)

    async def handle_chat_packet(self, packet):
        await self.log_unregistered_packet(packet)