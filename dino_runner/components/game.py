from pdb import Restart
import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.score import Score

from dino_runner.utils.constants import BG, DEFAULT_TYPE, DINO_START, FONT_STYLE, GAME_OVER, ICON, RESET, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE, TITLE, FPS

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.death_count = 0
        self.score = Score()
        self.power_up_manager = PowerUpManager()


    def run(self): 
        self.executing = True 
        while self.executing:
            if not self.playing:
                self.show_menu()

        pygame.quit()       

    def start_game(self):
        # Game loop: events - update - draw
        self.game_speed = 20 
        self.playing = True
        self.score.reset()
        self.obstacle_manager.reset()
        self.power_up_manager.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed, self.player, self.on_death)
        self.score.update(self, self.playing)
        self.power_up_manager.update(self.game_speed, self.score.score, self.player)
       

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.player.check_power_up(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def on_death(self):
        self.playing = False
        self.death_count += 1
       
    def show_menu(self):
        #Llenar pantalla en blanco 
        self.screen.fill((255,255,255))
        font = pygame.font.Font(FONT_STYLE, 32)
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        x = 360
        y = 200
        x_1 = 510
        y_1 = 250
        #Mensaje de bienvenida centrado
        if not self.death_count:
            text = font.render("Welcome, press any key to start!", True,(0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect)  
            self.screen.blit(DINO_START,(half_screen_width - 40, half_screen_height - 140))
        elif self.death_count:
            font = pygame.font.Font(FONT_STYLE, 15)
            text = font.render("Press any key to restart!", True,(0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height + 40)
            self.screen.blit(text, text_rect)  
            self.screen.blit(GAME_OVER, (x, y))
            self.screen.blit(RESET, (x_1, y_1))

            deaths_draw_text = half_screen_height + 75
            score_draw_text = half_screen_height + 100
            deaths = f"Deaths: {self.death_count}" 
            score = f"Score: {self.score.update(self, self.playing)}"
            self.draw_text(half_screen_height, deaths_draw_text, deaths, 20)
            self.draw_text(half_screen_height, score_draw_text, score, 20)

        #Plasmar cambios
        pygame.display.update()
        #Manejar los eventos
        self.handle_menu_events()
    
    def draw_text(self, x, y, text, size):
        font = pygame.font.Font(FONT_STYLE, size)
        text = font.render(text, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text, text_rect)  
    
    def check_power_up(self, screen):
        if self.type == SHIELD_TYPE:
            time_to_show = round(
                (self.power_up_time_up- pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                self.draw_text(f"{self.type.capitalize()} enabled for {time_to_show} seconds.",
                              screen, font_size=16, pos_y_center=50)
            else:
                self.type = DEFAULT_TYPE 
                self.power_up_time_up = 0
        


    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
            
            if event.type == pygame.KEYDOWN:
                self.start_game()
    