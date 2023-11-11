from .gameobject import GameObject

class Player(GameObject):
    def __init__(self, scene, x, y):
        super().__init__(scene, x, y)
        self.image = self.scene.game.image_manager['player']
        self.speed = 200

    def update(self, delta):
        if self.scene.game.input_manager.is_pressed('left'):
            self.x -= self.speed * delta
        if self.scene.game.input_manager.is_pressed('right'):
            self.x += self.speed * delta
        if self.scene.game.input_manager.is_pressed('up'):
            self.y -= self.speed * delta
        if self.scene.game.input_manager.is_pressed('down'):
            self.y += self.speed * delta

    def draw(self):
        self.scene.game.screen.blit(self.image, (self.x, self.y))