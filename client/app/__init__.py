import threading
import pygame
from pygame.locals import *
from app.game.input_manager import InputManager
from app.game.scene import Scene, entry_scene
from app.net.network import NetworkManager
from app.ui.gui_controls import Text

class App:
    _instance = None  # private class attribute to hold the singleton instance

    def __new__(cls, *args, **kwargs):
        """ensure only one instance is created."""
        if cls._instance is None:
            cls._instance = super(App, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Ensure initialization happens only once
        if not hasattr(self, '_initialized'):
            pygame.init()
            self.screen = pygame.display.set_mode((800, 600))
            pygame.display.set_caption("Moonlapse")
            self.running = True
            self._initialized = True
            self.input_manager = InputManager()

            # start the network manager on a separate thread
            self.network_manager = NetworkManager()
            self.network_thread = threading.Thread(target=self.network_manager.start, daemon=True)
            self.network_thread.start()

            self.scene = entry_scene()

    def run(self):
        """Main event loop."""
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))  # clear the screen with black color
            self.scene.update()
            self.scene.draw(self.screen)

            pygame.display.update()

        pygame.quit()

    @classmethod
    def get_current_app(cls):
        """get the single instance of the app."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
def get_current_app():
    return App.get_current_app()