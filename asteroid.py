import random

import pygame

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def split(self):
        """asteroid splitting function"""
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_asteroid_1 = self.velocity.rotate(+random_angle)
        new_asteroid_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = new_asteroid_1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = new_asteroid_2 * 1.2

    def update(self, dt):
        self.position += self.velocity * dt