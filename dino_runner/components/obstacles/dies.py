import pygame
from dino_runner.utils.constants import FONT_STYLE

class Dies():
    def __init__(self):
        self.dies = 0

    def update(self):
        self.dies += 1

    def draw(self, screen): 
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Dies: {self.dies}", True, (0, 0, 0)) 
        text_rect = text.get_rect()
        text_rect.center = (800, 30)
        screen.blit(text, text_rect)