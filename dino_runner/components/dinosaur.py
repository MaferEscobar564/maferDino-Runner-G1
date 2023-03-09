import pygame
from pygame.sprite import Sprite
from dino_runner.components.text import Text

from dino_runner.utils.constants import DEFAULT_TYPE, DUCKING_HAMMER, DUCKING_SHIELD, FONT_STYLE, HAMMER_TYPE, JUMPING, JUMPING_HAMMER, JUMPING_SHIELD, RUNNING, DUCKING, RUNNING_HAMMER, RUNNING_SHIELD, SHIELD_TYPE 


DINO_RUNNING = "running"
DINO_JUMPING = "jumping"
DINO_DUCKING = "ducking"

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER }
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}

class Dinosaur(Sprite): #El () en una clase es para indicar que se va a extraer algo de otro archivo py. 
    POSITION_X = 80
    POSITION_Y = 310
    JUMP_VELOCITY = 8.5

    def __init__(self): 
        self.type = DEFAULT_TYPE
        self.power_up_time_up = 0
        self.image = RUN_IMG[self.type][0]
        self.rect = self.image.get_rect()
        self.rect.x = self.POSITION_X
        self.rect.y = self.POSITION_Y

        self.step = 0
        self.action = DINO_RUNNING
        self.jump_velocity = self.JUMP_VELOCITY
        self.text = Text()
    
    def update(self, user_input):
       if self.action == DINO_RUNNING: 
           self.run()
       elif self.action == DINO_JUMPING:
           self.jump()
       elif self.action == DINO_DUCKING:
           self.duck()
       
       if self.action != DINO_JUMPING: 
            if user_input[pygame.K_UP]:
               self.action = DINO_JUMPING 
            elif user_input[pygame.K_DOWN]:
               self.action = DINO_DUCKING
            else:
               self.action = DINO_RUNNING

       if self.step >= 10:
           self.step = 0
    
    def duck(self):
        self.image = DUCK_IMG[self.type][self.step // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.POSITION_X
        self.rect.y = 350
        self.step += 1

    def jump(self):
        self.image = JUMP_IMG[self.type]
        self.rect.y -= self.jump_velocity *4
        self.jump_velocity -= 0.8
        print("VELOCITY ::", self.jump_velocity)
        print("Y ::", self.rect.y)
        if self.jump_velocity < - self.JUMP_VELOCITY:
               self.jump_velocity = self.JUMP_VELOCITY
               self.action = DINO_RUNNING
               self.rect.y = self.POSITION_Y
        
    def run(self):
        self.image = RUN_IMG[self.type][self.step // 5] 
        self.rect = self.image.get_rect()
        self.rect.x = self.POSITION_X
        self.rect.y = self.POSITION_Y 
        self.step += 1

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def on_pick_power_up (self, power_up): 
        self.type = power_up.type 
        self.power_up_time_up = power_up.start_time +\
              (power_up.duration * 1000)
        
    def check_power_up(self, screen):
        if self.type == SHIELD_TYPE or self.type == HAMMER_TYPE:
            time_to_show = round((self.power_up_time_up- pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                self.text.show(100, 350, f"{self.type.capitalize()} enabled for {time_to_show} seconds.", 18, screen)

    