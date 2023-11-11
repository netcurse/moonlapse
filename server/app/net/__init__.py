from .packets_pb2 import LoginPacket, ChatPacket, RegisterPacket, Packet, DenyPacket, OkPacket, HeartbeatPacket

def create_login_packet(user: str, password: str):
    login_packet = LoginPacket()
    login_packet.username = user
    login_packet.password = password
    packet = Packet()
    packet.login.CopyFrom(login_packet)
    return packet

def create_register_packet(user: str, password: str):
    register_packet = RegisterPacket()
    register_packet.username = user
    register_packet.password = password
    packet = Packet()
    packet.register.CopyFrom(register_packet)
    return packet

def create_chat_packet(user: str, message: str):
    chat_packet = ChatPacket()
    chat_packet.name = user
    chat_packet.message = message
    packet = Packet()
    packet.chat.CopyFrom(chat_packet)
    return packet

def create_deny_packet(reason: str):
    deny_packet = DenyPacket()
    deny_packet.reason = reason
    packet = Packet()
    packet.deny.CopyFrom(deny_packet)
    return packet

def create_ok_packet(reason: str):
    ok_packet = OkPacket()
    ok_packet.reason = reason
    packet = Packet()
    packet.ok.CopyFrom(ok_packet)
    return packet

def create_heartbeat_packet():
    heartbeat_packet = HeartbeatPacket()
    packet = Packet()
    packet.heartbeat.CopyFrom(heartbeat_packet)
    return packet