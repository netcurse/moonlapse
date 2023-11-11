

class GameObject:
    def __init__(self, scene, x, y):
        self.scene = scene
        self.x = x
        self.y = y

    def init(self):
        """Called after the scene is loaded"""
        pass

    def update(self):
        """Called every frame"""
        pass

    def draw(self, screen):
        """Called every frame"""
        pass

    def destroy(self):
        self.scene.objects.remove(self)