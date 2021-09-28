import random
import pygame

from nlc_dino_runner.components.obstacles.bird import Bird
from nlc_dino_runner.components.obstacles.cactus import Cactus
from nlc_dino_runner.components.obstacles.snake import Snake
from nlc_dino_runner.utils.constants import BIRD, SMALL_CACTUS, LARGE_CACTUS, SNAKE


class ObstaclesManager:
    def __init__(self):
        self.obstacles_list = []

    def update(self, game, points, user_input):
        game.player.dino_game_over = False

        if len(self.obstacles_list) == 0:
            cactus = Cactus(random.choice([SMALL_CACTUS, LARGE_CACTUS]))
            bird = Bird(BIRD)
            snake = Snake(SNAKE)
            if points >= 1000:
                obstacles = random.choice([cactus, bird, snake])
            else:
                obstacles = random.choice([cactus, bird])
            self.obstacles_list.append(obstacles)

        for obstacle in self.obstacles_list:
            obstacle.update(game.game_speed, self.obstacles_list)
            if game.power_up_manager.hammer.rect.colliderect(obstacle.rect):
                if obstacle in self.obstacles_list:
                    self.obstacles_list.remove(obstacle)
            if game.power_up_manager.shuriken.rect.colliderect(obstacle.rect):
                if obstacle in self.obstacles_list:
                    self.obstacles_list.remove(obstacle)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    if obstacle in self.obstacles_list:
                        self.obstacles_list.remove(obstacle)
                elif game.player.chainsaw and user_input[pygame.K_SPACE] and (obstacle.image == SMALL_CACTUS or
                                                                              obstacle.image == LARGE_CACTUS):
                    if obstacle in self.obstacles_list:
                        self.obstacles_list.remove(obstacle)
                elif game.player.sword:
                    if obstacle in self.obstacles_list:
                        self.obstacles_list.remove(obstacle)
                elif game.player.halberd and user_input[pygame.K_SPACE]:
                    if obstacle in self.obstacles_list:
                        self.obstacles_list.remove(obstacle)
                else:
                    hit_sound = pygame.mixer.Sound('sounds/obstacles/hit_a_obstacle.wav')
                    hit_sound.play()
                    game.lives_manager.reduce_lives()
                    if obstacle in self.obstacles_list:
                        self.obstacles_list.remove(obstacle)
                    if game.lives_manager.number_of_lives == 0:
                        death_sound = pygame.mixer.Sound('sounds/game_over.wav')
                        death_sound.play()
                        game.death_count += 1
                        game.player.dino_game_over = True
                        game.playing = False

    def draw(self, screen):
        for obstacle in self.obstacles_list:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles_list = []
