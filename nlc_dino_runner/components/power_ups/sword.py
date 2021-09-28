from nlc_dino_runner.components.power_ups.power_up import PowerUp
from nlc_dino_runner.utils.constants import SWORD_RESIZED, SWORD_TYPE


class Sword(PowerUp):
    def __init__(self):
        self.image = SWORD_RESIZED
        self.type = SWORD_TYPE
        super().__init__(self.image, self.type)

    def initial_position(self, dino_rect):
        self.rect.x = dino_rect.x
        self.rect.y = dino_rect.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

