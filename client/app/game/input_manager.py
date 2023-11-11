import pygame

class InputManager:
    """Manage input from the user."""

    def __init__(self):
        self._current_keys = {}
        self._previous_keys = {}
        self._mouse_buttons = {}
        self._mouse_position = (0, 0)

    def update(self):
        """Update the input manager."""
        self._previous_keys = self._current_keys.copy()
        self._current_keys = pygame.key.get_pressed()
        self._mouse_buttons = pygame.mouse.get_pressed()
        self._mouse_position = pygame.mouse.get_pos()

    def is_key_pressed(self, key: int) -> bool:
        """Check if a key is pressed."""
        return self._current_keys[key]

    def is_key_just_pressed(self, key: int) -> bool:
        """Check if a key is just pressed."""
        return self._current_keys[key] and not self._previous_keys.get(key, False)

    def is_mouse_button_pressed(self, button: int) -> bool:
        """Check if a mouse button is pressed."""
        return self._mouse_buttons[button]

    def get_mouse_position(self) -> tuple:
        """Get the mouse position."""
        return self._mouse_position
