from nlc_dino_runner.components.power_ups.power_up import PowerUp
from nlc_dino_runner.utils.constants import HALBERD_RESIZED, HALBERD_TYPE


class Halberd(PowerUp):
    def __init__(self):
        self.image = HALBERD_RESIZED
        self.type = HALBERD_TYPE
        super().__init__(self.image, self.type)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
