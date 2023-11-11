import threading
import socket
from typing import List
from .packets import Packet

class NetworkManager:
    _instance = None  # private class attribute to hold the singleton instance

    def __new__(cls, *args, **kwargs):
        """ensure only one instance is created."""
        if cls._instance is None:
            cls._instance = super(NetworkManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        # Ensure initialization happens only once
        if not hasattr(self, '_initialized'):
            # todo: obviously change port and host
            self.port = 42523
            self.host = 'localhost'
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            self.incoming_packets: List[Packet] = []
            self.outgoing_packets: List[Packet] = []

            self.running = False

    def start(self):
        self.socket.connect((self.host, self.port))
        self.running = True
        
        while self.running:
            packet = self.read_packet()
            if packet:
                self.incoming_packets.append(packet)
            self.update()

    def send_packet(self, packet):
        data = packet.SerializeToString()
        length_prefix = len(data).to_bytes(4, byteorder='big')
        self.socket.sendall(length_prefix + data)

    def read_packet(self):
        length_prefix = self.socket.recv(4)
        if not length_prefix:
            return None
        length = int.from_bytes(length_prefix, byteorder='big')
        data = b''
        while len(data) < length:
            chunk = self.socket.recv(length - len(data))
            if not chunk:
                raise RuntimeError("socket connection broken")
            data += chunk
        packet = Packet.FromString(data)
        return packet

    def update(self):
        for packet in self.outgoing_packets:
            self.send(packet)
        self.outgoing_packets.clear()

    @classmethod
    def get_current_network_manager(cls):
        """get the single instance of the network manager."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
def get_current_network_manager():
    return NetworkManager.get_current_network_manager()
