import socket
import unittest
import socket_funcs as sf

class TestProtocol(unittest.TestCase):
    def setUp(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(sf.SERVER_ADDRESS)

    def tearDown(self):
        self.s.close()

    def test_send_login_packet(self):
        packet = sf.create_login_packet()
        sf.send_packet(self.s, packet)
        p = sf.read_packet(self.s)
        self.assertIsNotNone(p.ok)

    def test_send_register_packet(self):
        packet = sf.create_register_packet()
        sf.send_packet(self.s, packet)
        p = sf.read_packet(self.s)
        self.assertIsNotNone(p.ok)

    # def test_send_chat_packet(self):
    #     """This test expects a deny packet because the server is not expecting a chat packet in the Entry state."""
    #     packet = sf.create_chat_packet()
    #     sf.send_packet(self.s, packet)
    #     p = sf.read_packet(self.s)
    #     self.assertIsNotNone(p.deny)

    # def test_login_then_chat(self):
    #     login_packet = sf.create_login_packet()
    #     sf.send_packet(self.s, login_packet)
    #     chat_packet = sf.create_chat_packet()
    #     sf.send_packet(self.s, chat_packet)
    
    # def test_send_broken_packet(self):
    #     """This test expects no packet because the server receives a bad packet. Specifically, the length bytes are greater than the maximum packet size when interpreted as an integer."""
    #     garbage = b'garbage'
    #     self.s.sendall(garbage)

    # def test_send_incorrect_length_broken_packet(self):
    #     """This test expects no response (and connection to close) because the server will time out trying to read the length bytes."""
    #     garbage = b'\x00\x00\x10\x00garbage'
    #     self.s.sendall(garbage)

    # def test_send_incorrect_length_ok_packet(self):
    #     """This test expects no response (and connection to close) because the server will time out trying to read the length bytes."""
    #     garbageLen = b'\x00\x00\x10\x00'
    #     packet = sf.create_login_packet()
    #     garbage = garbageLen + packet.SerializeToString()
    #     self.s.sendall(garbage)
        