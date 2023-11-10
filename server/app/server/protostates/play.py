from .protostate import ProtoState

class PlayState(ProtoState):
    async def handle_chat_packet(self, packet):
        print("chat packet received")