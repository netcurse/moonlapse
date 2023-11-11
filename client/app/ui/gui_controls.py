from typing import Tuple

from pygame import Color
import pygame

class GuiControl:
    """
    Base class for all GUI controls.
    """

    def __init__(self, controller, pos: Tuple[int, int]):
        self.controller = controller
        self.pos = pos

    def update(self):
        pass

    def draw(self, screen):
        pass
        
class Text(GuiControl):
    """Create a text object."""

    def __init__(self, text: str, pos: Tuple[int, int], controller, fontname='app/assets/fonts/Consolas.ttf', fontsize=14, fontcolor=Color('white')):
        super().__init__(controller, pos)
        self.text = text
        self.pos = pos

        self.fontname = fontname
        self.fontsize = fontsize
        self.fontcolor = fontcolor
        self.set_font()
        self.render()

    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self, screen: pygame.Surface):
        """Draw the text image to the screen."""
        screen.blit(self.img, self.rect)


class Button(GuiControl):
    """Create a button."""

    def __init__(self, text: str, pos: Tuple[int, int], controller, action=None):
        super().__init__(controller, pos)
        self.text = Text(text, pos)
        self.pos = pos
        self.action = action    # a submit button would call controller.on_submit(), perhaps

    def draw(self, screen: pygame.Surface):
        self.text.draw(screen)

    def update(self):
        pass