from .gameobject import GameObject
from app.net.packets import create_login_packet, create_register_packet, create_chat_packet
from app.net.network import get_current_network_manager
from app import get_current_app
import pygame

class EntrySceneManager(GameObject):
    def __init__(self, scene):
        super().__init__(scene, 0, 0)

    def init(self):
        # login with fake credentials for demo
        pass

    def update(self):
        # process incoming packets (one packet per frame - TODO: fix this?)
        if len(get_current_network_manager().incoming_packets) > 0:
            packet = get_current_network_manager().incoming_packets.pop(0)
            self.process_packet(packet)

        # demo input handling
        if get_current_app().input_manager.key_just_pressed(pygame.K_r):
            username = "test"
            password = "test123"
            p = create_register_packet(username, password)
            get_current_network_manager().outgoing_packets.append(p)

        if get_current_app().input_manager.key_just_pressed(pygame.K_l):
            username = "test"
            password = "test123"
            p = create_login_packet(username, password)
            get_current_network_manager().outgoing_packets.append(p)

        if get_current_app().input_manager.key_just_pressed(pygame.K_c):
            p = create_chat_packet("test_fake_user", "Hello, world!")
            get_current_network_manager().outgoing_packets.append(p)
        

    def process_packet(self, packet):
        if packet.HasField('ok'):
            print(packet.ok.reason)
            # self.scene.game.scene_manager.change_scene('game')
        elif packet.HasField('deny'):
            print(packet.deny.reason)