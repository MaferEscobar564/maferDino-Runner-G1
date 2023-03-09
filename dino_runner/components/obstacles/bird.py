import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):

    def __init__(self):
       bird_type = 0
       image = BIRD[bird_type]
       super().__init__(image)
       self.rect.y = 320 and 290 and 250  
       self.step = 0  

    def update(self, game_speed, obstacle):
        super().update(game_speed, obstacle)
        self.image = BIRD[self.step // 5]
        self.step += 1
         
        if self.step >= 10:
            self.step = 0 

         
        
        

