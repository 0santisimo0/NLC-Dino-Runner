import pygame
from pygame.sprite import Sprite
from nlc_dino_runner.utils.text_utils import FONT_STYLE
from nlc_dino_runner.utils.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    DEFAULT_TYPE,
    SHIELD_TYPE,
    HAMMER_TYPE,
    CHAINSAW_TYPE,
    SHURIKEN_TYPE,
    SWORD_TYPE,
    HALBERD_TYPE,
    RUNNING,
    DUCKING,
    JUMPING,
    RUNNING_SHIELD,
    DUCKING_SHIELD,
    JUMPING_SHIELD,
    RUNNING_HAMMER,
    DUCKING_HAMMER,
    JUMPING_HAMMER,
    RUNNING_CHAINSAW,
    DUCKING_CHAINSAW,
    JUMPING_CHAINSAW,
    RUNNING_SHURIKEN,
    DUCKING_SHURIKEN,
    JUMPING_SHURIKEN,
    RUNNING_SWORD,
    DUCKING_SWORD,
    JUMPING_SWORD,
    RUNNING_HALBERD,
    DUCKING_HALBERD,
    JUMPING_HALBERD,
    DINO_DEAD,
    DINO_DEAD_DUCK,
    GAME_OVER
)


class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 9.5

    def __init__(self):
        self.run_img = {
            DEFAULT_TYPE: RUNNING,
            SHIELD_TYPE: RUNNING_SHIELD,
            HAMMER_TYPE: RUNNING_HAMMER,
            CHAINSAW_TYPE: RUNNING_CHAINSAW,
            SHURIKEN_TYPE: RUNNING_SHURIKEN,
            SWORD_TYPE: RUNNING_SWORD,
            HALBERD_TYPE: RUNNING_HALBERD
            }
        self.jump_img = {
            DEFAULT_TYPE: JUMPING,
            SHIELD_TYPE: JUMPING_SHIELD,
            HAMMER_TYPE: JUMPING_HAMMER,
            CHAINSAW_TYPE: JUMPING_CHAINSAW,
            SHURIKEN_TYPE: JUMPING_SHURIKEN,
            SWORD_TYPE: JUMPING_SWORD,
            HALBERD_TYPE: JUMPING_HALBERD
            }
        self.duck_img = {
            DEFAULT_TYPE: DUCKING,
            SHIELD_TYPE: DUCKING_SHIELD,
            HAMMER_TYPE: DUCKING_HAMMER,
            CHAINSAW_TYPE: DUCKING_CHAINSAW,
            SHURIKEN_TYPE: DUCKING_SHURIKEN,
            SWORD_TYPE: DUCKING_SWORD,
            HALBERD_TYPE: DUCKING_HALBERD
            }
        self.type = DEFAULT_TYPE
        self.image = self.run_img[self.type][0]
        self.show_text = False
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
        self.dino_rect_duck = self.dino_rect
        self.dino_rect_run = self.dino_rect
        self.step_index = 0
        self.shield = False
        self.shield_time_up = 0
        self.hammer = False
        self.hammer_time_up = 0
        self.chainsaw = False
        self.chainsaw_time_up = 0
        self.shuriken = False
        self.shuriken_time_up = 0
        self.sword = False
        self.sword_time_up = 0
        self.halberd = False
        self.halberd_time_up = 0
        self.halberd_kill_activate = False
        self.dino_game_over = False
        self.image_game_over = GAME_OVER[0]
        self.image_game_over_rect = self.image_game_over.get_rect()
        self.image_game_over_rect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4

    def update(self, user_input):
        if self.dino_jump:
            self.jump()

        if self.dino_duck:
            self.duck()

        if self.dino_run:
            self.run()

        if user_input[pygame.K_DOWN] and not self.dino_jump:
            jump_sound = pygame.mixer.Sound('sounds/dino/action.wav')
            jump_sound.play()
            self.dino_duck = True
            self.dino_jump = False
            self.dino_run = False
        elif user_input[pygame.K_UP] and not self.dino_jump:
            duck_sound = pygame.mixer.Sound('sounds/dino/action.wav')
            duck_sound.play()
            self.dino_jump = True
            self.dino_duck = False
            self.dino_run = False
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.image = self.run_img[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.dino_rect_run = self.dino_rect
        self.step_index += 1

    def duck(self):
        self.image = self.duck_img[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.dino_rect_duck = self.dino_rect
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img[self.type]

        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 1

        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def check_time(self, screen, black):
        font = pygame.font.Font(FONT_STYLE, 20)
        black_color = (0, 0, 0)
        white_color = (255, 255, 255)

        if self.shield:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks()) / 1000, 1)
            if time_to_show == 0:
                shield_sound = pygame.mixer.Sound('sounds/power_ups/shield.ogg')
                shield_sound.play()
                self.shield = False
                if self.type == SHIELD_TYPE:
                    self.type = DEFAULT_TYPE
            else:
                if self.show_text:
                    if not black:
                        text = font.render(f'Shield enabled for: {time_to_show}', True, black_color)
                    else:
                        text = font.render(f'Shield enabled for: {time_to_show}', True, white_color)
                    text_rect = (450, 40)
                    screen.blit(text, text_rect)
        elif self.hammer:
            time_to_show = round((self.hammer_time_up - pygame.time.get_ticks()) / 1000, 1)
            if time_to_show == 0:
                hammer_sound = pygame.mixer.Sound('sounds/power_ups/hammer.ogg')
                hammer_sound.play()
                self.hammer = False
                if self.type == HAMMER_TYPE:
                    self.type = DEFAULT_TYPE
            else:
                if self.show_text:
                    if not black:
                        text = font.render(f'Hammer enabled for: {time_to_show}', True, black_color)
                    else:
                        text = font.render(f'Hammer enabled for: {time_to_show}', True, white_color)
                    text_rect = (450, 40)
                    screen.blit(text, text_rect)
        elif self.chainsaw:
            time_to_show = round((self.chainsaw_time_up - pygame.time.get_ticks()) / 1000, 1)
            if time_to_show == 0:
                chainsaw_sound = pygame.mixer.Sound('sounds/power_ups/chainsaw.wav')
                chainsaw_sound.play()
                self.chainsaw = False
                if self.type == CHAINSAW_TYPE:
                    self.type = DEFAULT_TYPE
            else:
                if self.show_text:
                    if not black:
                        text = font.render(f'Chainsaw enabled for: {time_to_show}', True, black_color)
                    else:
                        text = font.render(f'Chainsaw enabled for: {time_to_show}', True, white_color)
                    text_rect = (450, 40)
                    screen.blit(text, text_rect)
        elif self.shuriken:
            time_to_show = round((self.shuriken_time_up - pygame.time.get_ticks()) / 1000, 1)
            if time_to_show == 0:
                shuriken_sound = pygame.mixer.Sound('sounds/power_ups/shuriken.wav')
                shuriken_sound.play()
                self.shuriken = False
                if self.type == SHURIKEN_TYPE:
                    self.type = DEFAULT_TYPE
            else:
                if self.show_text:
                    font = pygame.font.Font(FONT_STYLE, 20)
                    black_color = (0, 0, 0)
                    white_color = (255, 255, 255)
                    if not black:
                        text = font.render(f'Shuriken enabled for: {time_to_show}', True, black_color)
                    else:
                        text = font.render(f'Shuriken enabled for: {time_to_show}', True, white_color)
                    text_rect = (450, 40)
                    screen.blit(text, text_rect)
        elif self.sword:
            time_to_show = round((self.sword_time_up - pygame.time.get_ticks()) / 1000, 1)
            if time_to_show == 0:
                sword_sound = pygame.mixer.Sound('sounds/power_ups/sword.wav')
                sword_sound.play()
                self.sword = False
                if self.type == SWORD_TYPE:
                    self.type = DEFAULT_TYPE
            else:
                if self.show_text:
                    font = pygame.font.Font(FONT_STYLE, 20)
                    black_color = (0, 0, 0)
                    white_color = (255, 255, 255)
                    if not black:
                        text = font.render(f'Sword enabled for: {time_to_show}', True, black_color)
                    else:
                        text = font.render(f'Sword enabled for: {time_to_show}', True, white_color)
                    text_rect = (450, 40)
                    screen.blit(text, text_rect)
        elif self.halberd:
            time_to_show = round((self.halberd_time_up - pygame.time.get_ticks()) / 1000, 1)
            if time_to_show == 0:
                halberd_sound = pygame.mixer.Sound('sounds/power_ups/halberd.wav')
                halberd_sound.play()
                self.halberd = False
                if self.type == HALBERD_TYPE:
                    self.type = DEFAULT_TYPE
            else:
                if self.show_text:
                    font = pygame.font.Font(FONT_STYLE, 20)
                    black_color = (0, 0, 0)
                    white_color = (255, 255, 255)
                    if not black:
                        text = font.render(f'Halberd enabled for: {time_to_show}', True, black_color)
                    else:
                        text = font.render(f'Halberd enabled for: {time_to_show}', True, white_color)
                    text_rect = (450, 40)
                    screen.blit(text, text_rect)

    def draw(self, screen, black):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        self.print_game_over(screen, black)

    def print_game_over(self, screen, black):
        if self.dino_game_over:
            self.draw_player_dead(screen)

            if black:
                self.image_game_over = GAME_OVER[1]

            screen.blit(self.image_game_over, self.image_game_over_rect)
            pygame.display.flip()
            pygame.time.delay(2000)

    def draw_player_dead(self, screen):
        if self.dino_rect == self.dino_rect_duck:
            screen.blit(DINO_DEAD_DUCK, self.dino_rect)
        else:
            screen.blit(DINO_DEAD, self.dino_rect)
