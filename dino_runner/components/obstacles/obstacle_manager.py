import pygame, random
from dino_runner.components.obstacles.cactus import SmallCactus, LargeCactus
from dino_runner.components.obstacles.obstacle import Obstacle

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game_speed, player, game):
        if not self.obstacles:
            Cactus_obstacle = random.randint(0, 2)
            if Cactus_obstacle == 0:
                self.obstacles.append(SmallCactus())
            elif Cactus_obstacle == 1:
                self.obstacles.append(LargeCactus())

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if player.rect.colliderect(obstacle.rect): 
                pygame.time.delay(500)
                game.playing = False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)     
            
                
            