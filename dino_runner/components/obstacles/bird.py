import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
     def __init__(self):
        bird_type = 0
        image = BIRD[bird_type]
        super().__init__(image)
        self.rect.y = 250 

        


        

