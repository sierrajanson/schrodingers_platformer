import pygame

class Animation:
    """inspired by Milo's description of the animation object in his game engine"""

    def __init__(self, screen, frames):
        self.frames = frames
        self.screen = screen
        self.index = 0
        self.start_time = pygame.time.get_ticks()

    def animate(self, position, fps = 1, velocity=None):
        current_time = pygame.time.get_ticks()
        current_frame = self.frames[self.index]
        if velocity.x > 0:
             current_frame = pygame.transform.flip(current_frame, True, False)
        self.screen.blit(current_frame, position)
        if velocity.x != 0 and current_time - self.start_time >= 1000/fps:
            self.index = (self.index + 1) % len(self.frames)
            self.start_time = current_time