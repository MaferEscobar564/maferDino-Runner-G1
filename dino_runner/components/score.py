import pygame
from dino_runner.utils.constants import FONT_STYLE, HAMMER_TYPE

class Score():
    def __init__(self):
        self.score = 0

    def update(self, game, playing):
        if playing == True:
            self.score += 1    
        else:
            self.score -= 0
        
        if self.score == HAMMER_TYPE and self.score % 0 == 0:
            game.game_speed == 0
        elif self.score % 100 == 0: 
            game.game_speed += 2
            
        return self.score
    
    def reset(self):
        self.score = 0

    def draw(self, screen): 
        font = pygame.font.Font(FONT_STYLE, 24)
        text = font.render(f"Score: {self.score}", True, (0, 0, 0)) 
        text_rect = text.get_rect()
        text_rect.center = (950, 30)
        screen.blit(text, text_rect)