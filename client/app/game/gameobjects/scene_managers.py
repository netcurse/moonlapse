from .gameobject import GameObject
from app.net.packets import create_login_packet

class EntrySceneManager(GameObject):
    def __init__(self, scene):
        super().__init__(scene, 0, 0)

    def init(self):
        # login with fake credentials for demo
        username = "test"
        password = "test123"
        p = create_login_packet(username, password)
        self.scene.game.network_manager.send_packet(p)
        pass