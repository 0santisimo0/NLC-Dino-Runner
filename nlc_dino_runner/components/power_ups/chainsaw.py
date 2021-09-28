from nlc_dino_runner.components.power_ups.power_up import PowerUp
from nlc_dino_runner.utils.constants import CHAINSAW, CHAINSAW_TYPE


class Chainsaw(PowerUp):
    def __init__(self):
        self.image = CHAINSAW
        self.type = CHAINSAW_TYPE
        super().__init__(self.image, self.type)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
