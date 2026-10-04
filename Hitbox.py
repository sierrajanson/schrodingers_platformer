import pygame
class Hitbox:
    def __init__(self, screen, position, width, height):
        self.position = position
        self.width = width
        self.height = height
        self.screen = screen

    def isColliding(self, other_hitbox):
        return False

    def draw(self):
        pygame.draw.rect(
            self.screen, (255, 192, 203), (self.position.x, self.position.y, self.width, self.height), 3)
