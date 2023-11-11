from app.game.gameobjects.scene_managers import EntrySceneManager
from app.ui.gui_controller import GuiController
from app.ui.gui_controls import GuiControl, Text


class Scene:
    def __init__(self, name):
        self.name = name
        self.objects = []
        self.gui_controls = []
        self.background = None

    def init(self):
        # todo: objects added later won't be initialized
        for obj in self.objects:
            obj.init()

    def update(self):
        for obj in self.objects:
            obj.update()
        for gui in self.gui_controls:
            gui.update()

    def draw(self, screen):
        if self.background:
            screen.blit(self.background, (0, 0))
        for obj in self.objects:
            obj.draw(screen)
        for gui in self.gui_controls:
            # GUI draws on top of everything else
            gui.draw(screen)

def entry_scene():
    scene = Scene("Entry")
    scene.objects.append(EntrySceneManager(scene))
    gui_controller = GuiController()
    scene.gui_controls.append(Text("Moonlapse: Press [R] to register, [L] to login", (20, 20), gui_controller))
    return scene

def game_scene():
    scene = Scene("Game")
    return scene