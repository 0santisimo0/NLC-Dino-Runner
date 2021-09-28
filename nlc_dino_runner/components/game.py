import pygame
import random

from nlc_dino_runner.components.dino import Dinosaur
from nlc_dino_runner.components.lives.lives_manager import LivesManager
from nlc_dino_runner.components.power_ups.power_up_manager import PowerUpManager
from nlc_dino_runner.components.obstacles.obstacle_manager import ObstaclesManager
from nlc_dino_runner.utils import text_utils
from nlc_dino_runner.utils.constants import TITLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, BG, FPS, CLOUD, RESTART


def background_music():
    pygame.mixer.music.load('sounds/background_song.mp3')
    pygame.mixer.music.play(-1)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)

        self.player = Dinosaur()
        self.lives_manager = LivesManager()
        self.obstacles_manager = ObstaclesManager()
        self.power_up_manager = PowerUpManager()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.restart_bottom = RESTART.get_rect()
        self.playing = False
        self.running = True
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = 0
        self.y_pos_cloud = random.randint(40, 150)
        self.game_speed = 20
        self.death_count = 0
        self.points = 0
        self.max_points = 0
        self.layer = 1
        self.max_layer = 0
        self.black = False
        self.green = False
        self.red = False

    def run(self):
        start_sound = pygame.mixer.Sound('sounds/start_and_restart.wav')
        start_sound.play()
        self.lives_manager.restart_lives()
        self.obstacles_manager.reset_obstacles()
        self.points = 0
        self.layer = 1
        self.power_up_manager.reset_power_ups(self.points, self.player)
        self.playing = True
        self.game_speed = 20

        while self.playing:
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacles_manager.update(self, self.points, user_input)
        self.power_up_manager.update(self.points, self.game_speed, self.player, user_input)

    def draw(self):
        self.clock.tick(FPS)
        self.handle_background_color_and_level()
        self.draw_background()
        self.score()
        self.max_score()
        self.level_counter()
        self.max_level()
        self.player.draw(self.screen, self.black)
        self.obstacles_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.lives_manager.print(self.screen, self.black)

        pygame.display.update()
        pygame.display.flip()

    def score(self):
        self.points += 1

        if self.points % 100 == 0:
            self.game_speed += 1

        score_element, score_element_rect = text_utils.get_score_element(self.points, self.black)
        self.screen.blit(score_element, score_element_rect)
        self.player.check_time(self.screen, self.black)

    def max_score(self):
        if self.max_points < self.points:
            self.max_points = self.points
        else:
            self.max_points = self.max_points

        max_score_element, max_score_element_rect = text_utils.get_max_score_element(self.max_points, self.black)
        self.screen.blit(max_score_element, max_score_element_rect)
        self.player.check_time(self.screen, self.black)

    def level_counter(self):
        if self.points == 1000:
            self.layer = 2
        elif self.points == 2000:
            self.layer = 3
        elif self.points == 3000:
            self.layer = 4
        elif self.points == 4000:
            self.layer = 'How?'

        level_element, level_element_rect = text_utils.get_level_element(self.layer, self.black)
        self.screen.blit(level_element, level_element_rect)
        self.player.check_time(self.screen, self.black)

    def max_level(self):
        if self.max_layer < self.layer:
            self.max_layer = self.layer
        else:
            self.max_layer = self.max_layer

        max_level_element, max_level_element_rect = text_utils.get_max_level_element(self.max_layer, self.black)
        self.screen.blit(max_level_element, max_level_element_rect)
        self.player.check_time(self.screen, self.black)

    def draw_background(self):
        if self.black:
            self.screen.fill((2, 2, 2))
        elif self.green:
            self.screen.fill((0, 255, 0))
        elif self.red:
            self.screen.fill((255, 0, 0))
        else:
            self.screen.fill((255, 255, 255))

        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        cloud_rect = CLOUD.get_rect()
        cloud_rect.midleft = (SCREEN_WIDTH, self.y_pos_cloud)
        self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))
        self.screen.blit(CLOUD, (cloud_rect.x + self.x_pos_cloud, self.y_pos_cloud))

        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))
            self.x_pos_bg = 0

        self.x_pos_bg -= self.game_speed

        if self.x_pos_cloud < -cloud_rect.right:
            self.screen.blit(CLOUD, (cloud_rect.x + self.x_pos_cloud, self.y_pos_cloud))
            self.y_pos_cloud = random.randint(50, 250)
            cloud_rect.left = 1200
            self.x_pos_cloud = 0

        self.x_pos_cloud -= self.game_speed / 2.5

    def execute(self):
        background_music()

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
            if self.death_count == 0 and event.type == pygame.KEYDOWN:
                self.run()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                if self.restart_bottom.collidepoint(click):
                    self.run()

    def handle_background_color_and_level(self):
        if self.points == 0:
            self.black = False
            self.green = False
            self.red = False
        elif self.points == 1000:
            self.black = True
        elif self.points == 2000:
            self.black = False
            self.green = True
        elif 3000 <= self.points <= 4000:
            self.green = False
            self.red = True
        else:
            self.red = False

    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT // 2

        if self.death_count == 0:
            text, text_rect = text_utils.get_centered_message("Press Any Key to Start")
            self.screen.blit(text, text_rect)
        else:
            self.restart_bottom.midtop = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.2)
            self.screen.blit(RESTART, self.restart_bottom)

            death_score, death_score_rect = text_utils.get_centered_message("Death count: " + str(self.death_count),
                                                                            height=half_screen_height)
            self.screen.blit(death_score, death_score_rect)
            points_score, points_score_rect = text_utils.get_centered_message("Score: " + str(self.points),
                                                                              height=half_screen_height + 40)
            self.screen.blit(points_score, points_score_rect)
            max_score, max_score_rect = text_utils.get_centered_message('Max Score: ' + str(self.max_points),
                                                                        height=half_screen_height + 80)
            self.screen.blit(max_score, max_score_rect)
            level, level_rect = text_utils.get_centered_message('Level Reached: ' + str(self.layer),
                                                                height=half_screen_height + 120)
            self.screen.blit(level, level_rect)
            max_level, max_level_rect = text_utils.get_centered_message('Max Level Reached: ' + str(self.max_layer),
                                                                        height=half_screen_height + 160)
            self.screen.blit(max_level, max_level_rect)

        self.screen.blit(ICON, ((SCREEN_WIDTH // 2) - 40, (SCREEN_HEIGHT // 2) - 150))
