import random
import pygame

from nlc_dino_runner.components.power_ups.shield import Shield
from nlc_dino_runner.components.power_ups.hammer import Hammer
from nlc_dino_runner.components.power_ups.chainsaw import Chainsaw
from nlc_dino_runner.components.power_ups.shuriken import Shuriken
from nlc_dino_runner.components.power_ups.sword import Sword
from nlc_dino_runner.components.power_ups.halberd import Halberd
from nlc_dino_runner.utils.constants import (
    DEFAULT_TYPE,
    SHIELD_TYPE,
    HAMMER_TYPE,
    CHAINSAW_TYPE,
    SHURIKEN_TYPE,
    SWORD_TYPE,
    HALBERD_TYPE,
    RUNNING_HALBERD_KILL,
    DUCKING_HALBERD_KILL
)


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.points = 0
        self.sword = Sword()
        self.hammer = Hammer()
        self.hammer_on_screen = False
        self.shuriken = Shuriken()
        self.shuriken_on_screen = False
        self.halberd = Halberd()
        self.halberd_kill_activate = False

    def reset_power_ups(self, points, player):
        self.power_ups = []
        self.points = points
        self.when_appears = random.randint(200, 300) + self.points
        self.hammer_on_screen = False
        self.shuriken_on_screen = False

        player.hammer_time_up = 0
        player.shuriken_time_up = 0
        player.sword_time_up = 0
        player.halberd_time_up = 0

    def generate_power_ups(self, points):
        self.points = points

        if len(self.power_ups) == 0:
            if self.when_appears == self.points:
                self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                self.power_ups.append(random.choice(
                    [
                        Shield(),
                        Hammer(),
                        Chainsaw(),
                        Shuriken(),
                        Sword(),
                        Halberd()
                     ]
                ))

    def update(self, points, game_speed, player, user_input):
        self.generate_power_ups(points)
        time_random = random.randrange(5, 8)

        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                if power_up.type == SHIELD_TYPE:
                    shield_sound = pygame.mixer.Sound('sounds/power_ups/shield.ogg')
                    shield_sound.play()
                    player.show_text = True
                    player.shield = True
                    player.hammer = False
                    player.chainsaw = False
                    player.shuriken = False
                    player.sword = False
                    player.halberd = False
                    player.type = power_up.type
                    power_up.start_time = pygame.time.get_ticks()
                    player.shield_time_up = power_up.start_time + (time_random * 1000)
                    self.power_ups.remove(power_up)
                elif power_up.type == HAMMER_TYPE:
                    hammer_sound = pygame.mixer.Sound('sounds/power_ups/hammer.ogg')
                    hammer_sound.play()
                    player.show_text = True
                    player.hammer = True
                    player.shield = False
                    player.chainsaw = False
                    player.shuriken = False
                    player.sword = False
                    player.halberd = False
                    player.type = power_up.type
                    power_up.start_time = pygame.time.get_ticks()
                    player.hammer_time_up = power_up.start_time + (time_random * 1000)
                    self.power_ups.remove(power_up)
                elif power_up.type == CHAINSAW_TYPE:
                    chainsaw_sound = pygame.mixer.Sound('sounds/power_ups/chainsaw.wav')
                    chainsaw_sound.play()
                    player.show_text = True
                    player.chainsaw = True
                    player.shield = False
                    player.hammer = False
                    player.shuriken = False
                    player.sword = False
                    player.halberd = False
                    player.type = power_up.type
                    power_up.start_time = pygame.time.get_ticks()
                    player.chainsaw_time_up = power_up.start_time + (time_random * 1000)
                    self.power_ups.remove(power_up)
                elif power_up.type == SHURIKEN_TYPE:
                    shuriken_sound = pygame.mixer.Sound('sounds/power_ups/shuriken.wav')
                    shuriken_sound.play()
                    player.show_text = True
                    player.shuriken = True
                    player.shield = False
                    player.hammer = False
                    player.chainsaw = False
                    player.sword = False
                    player.halberd = False
                    player.type = power_up.type
                    power_up.start_time = pygame.time.get_ticks()
                    player.shuriken_time_up = power_up.start_time + (time_random * 1000)
                    self.power_ups.remove(power_up)
                elif power_up.type == SWORD_TYPE:
                    sword_sound = pygame.mixer.Sound('sounds/power_ups/sword.wav')
                    sword_sound.play()
                    player.show_text = True
                    player.sword = True
                    player.shield = False
                    player.hammer = False
                    player.chainsaw = False
                    player.shuriken = False
                    player.halberd = False
                    player.type = power_up.type
                    power_up.start_time = pygame.time.get_ticks()
                    player.sword_time_up = power_up.start_time + (time_random * 1000)
                    self.power_ups.remove(power_up)
                elif power_up.type == HALBERD_TYPE:
                    halberd_sound = pygame.mixer.Sound('sounds/power_ups/halberd.wav')
                    halberd_sound.play()
                    player.show_text = True
                    player.halberd = True
                    player.shield = False
                    player.hammer = False
                    player.chainsaw = False
                    player.shuriken = False
                    player.sword = False
                    player.type = power_up.type
                    power_up.start_time = pygame.time.get_ticks()
                    player.halberd_time_up = power_up.start_time + (time_random * 1000)
                    self.power_ups.remove(power_up)

        # Hammer
        if user_input[pygame.K_SPACE] and player.hammer and not self.hammer_on_screen and player.hammer_time_up > 0:
            self.hammer_on_screen = True
            self.hammer.initial_position(player.dino_rect)
            if player.hammer_time_up == 0:
                player.type = DEFAULT_TYPE

        if self.hammer_on_screen:
            self.hammer.movement(game_speed, self)

        # Shuriken
        if user_input[pygame.K_SPACE] and player.shuriken and not self.shuriken_on_screen and player.shuriken_time_up > 0:
            self.shuriken_on_screen = True
            self.shuriken.initial_position(player.dino_rect)
            if player.shuriken_time_up == 0:
                player.type = DEFAULT_TYPE

        if self.shuriken_on_screen:
            self.shuriken.movement(game_speed, self)

        # Halberd
        if user_input[pygame.K_SPACE] and player.halberd and player.halberd_time_up > 0:
            player.halberd_kill_activate = True
            if player.dino_rect == player.dino_rect_duck:
                if player.step_index <= 5:
                    player.image = DUCKING_HALBERD_KILL[0]
                else:
                    player.image = DUCKING_HALBERD_KILL[1]
            elif player.dino_rect == player.dino_rect_run:
                if player.step_index <= 5:
                    player.image = RUNNING_HALBERD_KILL[0]
                else:
                    player.image = RUNNING_HALBERD_KILL[1]

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

        if self.hammer_on_screen:
            self.hammer.draw(screen)

        if self.shuriken_on_screen:
            self.shuriken.draw(screen)
