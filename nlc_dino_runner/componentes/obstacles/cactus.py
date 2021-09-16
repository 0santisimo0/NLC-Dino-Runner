from nlc_dino_runner.componentes.obstacles.obstacles import Obstacles
import random


class Cactus(Obstacles):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 320
