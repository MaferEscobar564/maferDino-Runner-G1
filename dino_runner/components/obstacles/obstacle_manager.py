import random
from dino_runner.components.obstacles.cactus import SmallCactus, LargeCactus
from dino_runner.components.obstacles.bird import Bird 

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game_speed, player, on_death):
        if not self.obstacles:
            Objects_obstacles = random.randint(0, 2)
            if  Objects_obstacles == 0:
                self.obstacles.append(SmallCactus())
            elif Objects_obstacles == 1:
                self.obstacles.append(LargeCactus())
            else: 
                self.obstacles.append(Bird())
                   
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if player.rect.colliderect(obstacle.rect): 
                on_death()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)   

    def reset(self):
        self.obstacles = []

       
            
                
            