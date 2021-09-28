from nlc_dino_runner.components.power_ups.power_up import PowerUp
from nlc_dino_runner.utils.constants import HAMMER, HAMMER_TYPE, SCREEN_WIDTH


class Hammer(PowerUp):
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super().__init__(self.image, self.type)

    def initial_position(self, dino_rect):
        self.rect.x = dino_rect.x
        self.rect.y = dino_rect.y

    def movement(self, game_speed, key):
        self.rect.x += game_speed + 5

        if self.rect.x >= SCREEN_WIDTH:
            self.rect.x = -200
            key.hammer_on_screen = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
