import logging
import trio
from app.database.engine import get_session_factory, init_engine
from app.server import protocol

class Core:
    def __init__(self, port: int):
        self.port = port
        self.engine = init_engine()
        self.SessionFactory = get_session_factory(self.engine)

    def run(self):
        logging.basicConfig(level=logging.INFO)
        logging.info(f"Server starting on port {self.port}")
        trio.run(trio.serve_tcp, self.handle_connection, self.port)

    async def handle_connection(self, server_stream: trio.SocketStream):
        logging.info(f"new connection started")

        proto = protocol.Protocol(server_stream, self)
        await proto.start()
