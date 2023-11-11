import pygame

class InputManager:
    """Manage input from the user."""

    def __init__(self):
        pygame.init()  # Ensure pygame is initialized
        self._current_keys = pygame.key.get_pressed()
        self._previous_keys = pygame.key.get_pressed()

    def update(self):
        """Update the input manager."""
        self._previous_keys = self._current_keys
        self._current_keys = pygame.key.get_pressed()

    def key_down(self, key: int) -> bool:
        """Check if a key is pressed."""
        return self._current_keys[key]

    def key_just_pressed(self, key: int) -> bool:
        """Check if a key is just pressed."""
        return self._current_keys[key] and not self._previous_keys[key]
