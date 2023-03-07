import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS 

class SmallCactus(Obstacle):
    def __init__(self): 
        cactus_type = random.randint(0, 2)
        image = SMALL_CACTUS[cactus_type]
        super().__init__(image)
        self.rect.y = 325

class LargeCactus(Obstacle):
    def __init__(self): 
        cactus_type = random.randint(0, 2)
        image = LARGE_CACTUS[cactus_type]
        super().__init__(image)
        self.rect.y = 300