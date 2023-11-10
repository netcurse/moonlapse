import packets
from packets import DenyPacket, Packet
from socket import socket, AF_INET, SOCK_STREAM

from tests.packets import packets_pb2

# assuming the server is running on localhost and port 42523
SERVER_ADDRESS = ('localhost', 42523)

def send_packet(sock, packet):
    data = packet.SerializeToString()
    length_prefix = len(data).to_bytes(4, byteorder='big')
    sock.sendall(length_prefix + data)

def read_packet(sock):
    length_prefix = sock.recv(4)
    if not length_prefix:
        return None
    length = int.from_bytes(length_prefix, byteorder='big')
    data = b''
    while len(data) < length:
        chunk = sock.recv(length - len(data))
        if not chunk:
            raise RuntimeError("socket connection broken")
        data += chunk
    packet = Packet.FromString(data)
    return packet

def create_login_packet():
    return packets.create_login_packet("testUser", "testPass")

def create_register_packet():
    return packets.create_register_packet("testUser", "testPass")

def create_chat_packet():
    return packets.create_chat_packet("testUser", "this is a test message.")
