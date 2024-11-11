"""import pygame"""

import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        """Circle Initialization Function"""
        # To be used later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        """draw function"""
        # sub-classes to override
        pass

    def update(self, screen):
        """update function"""
        # sub-classes to override
        pass

    def collision(self, other):
        return self.position.distance_to(other.position) <= (other.radius + self.radius)
