import pygame

from nlc_dino_runner.componentes.dinosaur import Dinosaur
from nlc_dino_runner.componentes.lives.lives_manager import LivesManager
from nlc_dino_runner.componentes.powerups.power_up_manager import PowerUpManager
from nlc_dino_runner.utils import text_utils
from nlc_dino_runner.componentes.obstacles.obstaclesManager import ObstaclesManager
from nlc_dino_runner.utils.constants import TITLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, BG, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.playing = False
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.game_speed = 20
        self.player = Dinosaur()
        self.obstacles_manager = ObstaclesManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.running = True
        self.death_count = 0
        self.lives_manager = LivesManager()

    def run(self):
        self.lives_manager.restart_lives()
        self.obstacles_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups(self.points)
        self.playing = True
        self.points = 0
        self.game_speed = 20
        while self.playing:
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                exit()

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacles_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.score()
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacles_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.lives_manager.print(self.screen)

        pygame.display.update()
        pygame.display.flip()

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        score_element, score_element_rect = text_utils.get_score_element(self.points)
        self.screen.blit(score_element, score_element_rect)
        self.player.check_invencibility(self.screen)

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))

        # la imagen se mueve
        self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))

        # Reset
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))
            self.x_pos_bg = 0

        self.x_pos_bg -= self.game_speed

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def show_menu(self):
        self.running = True

        white_color = (255, 255, 255)
        self.screen.fill(white_color)

        self.print_menu_elements()

        pygame.display.update()
        self.handle_key_events_on_menu()

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT // 2
        if self.death_count == 0:
            text, text_rect = text_utils.get_centered_message("Press Any Key to Start")
        else:
            text, text_rect = text_utils.get_centered_message("Press any Key to Restart")

        self.screen.blit(text, text_rect)

        death_score, death_score_rect = text_utils.get_centered_message("Death count: " + str(self.death_count),
                                                                        height=half_screen_height + 50)
        points_score, points_score_rect = text_utils.get_centered_message("Score: " + str(self.points),
                                                                          height=half_screen_height + 100)
        self.screen.blit(death_score, death_score_rect)
        self.screen.blit(ICON, ((SCREEN_WIDTH // 2) - 40, (SCREEN_HEIGHT // 2) - 150))
        self.screen.blit(points_score, points_score_rect)

# 'Clase 2: Ventana, background'
# Clase 4: Colisiones
# Clase 6.1
