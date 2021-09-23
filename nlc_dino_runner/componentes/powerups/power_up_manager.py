import random
import pygame

from nlc_dino_runner.componentes.powerups.hammer import Hammer
from nlc_dino_runner.componentes.powerups.shield import Shield
from nlc_dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE, DEFAULT_TYPE


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.points = 0
        self.hammer = Hammer()
        self.hammer_on_screen = False

    def reset_power_ups(self, points):
        self.power_ups = []
        self.points = points
        self.when_appears = random.randint(200, 300) + self.points
        self.hammer_on_screen = False

    def generate_power_ups(self, points):
        self.points = points

        if len(self.power_ups) == 0:
            if self.when_appears == self.points:
                print('generating power up')
                self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                self.power_ups.append(random.choice([Shield(), Hammer()]))

    def update(self, points, game_speed, player, user_input):
        self.generate_power_ups(points)

        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                if power_up.type == SHIELD_TYPE:
                    player.shield = True
                    player.show_text = True
                    player.hammer = False
                    player.type = power_up.type
                    power_up.start_time = pygame.time.get_ticks()
                    time_random = random.randrange(5, 8)
                    player.shield_time_up = power_up.start_time + (time_random * 1000)
                    self.power_ups.remove(power_up)
                elif power_up.type == HAMMER_TYPE:
                    player.hammer = True
                    player.show_text = True
                    player.shield = False
                    player.type = power_up.type
                    power_up.start_time = pygame.time.get_ticks()
                    time_random = random.randrange(5, 8)
                    player.hammer_time_up = power_up.start_time + (time_random * 1000)
                    self.power_ups.remove(power_up)

        if user_input[pygame.K_SPACE] and player.hammer and not self.hammer_on_screen and player.hammer_time_up > 0:
            self.hammer_on_screen = True
            self.hammer.initial_position(player.dino_rect)
            if player.hammer_time_up == 0:
                player.type = DEFAULT_TYPE

        if self.hammer_on_screen:
            self.hammer.movement(game_speed, self)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

        if self.hammer_on_screen:
            self.hammer.draw(screen)
