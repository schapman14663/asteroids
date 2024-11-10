# This allows us to use code from the open source
# pygame library throughout the file
"""import pygame library, constants.py"""
import pygame

from constants import *


def main():
    """Main Function For Asteroids Game"""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = (0, 0, 0)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color)
        pygame.display.flip()


if __name__ == "__main__":
    main()
