import random

from nlc_dino_runner.components.obstacles.obstacles import Obstacles


class Snake(Obstacles):
    def __init__(self, image):
        self.slide_index = 0
        self.index = 15
        self.move_state = False
        self.type = random.randint(0, 1)
        self.wait = random.randint(25, 30)
        super().__init__(image, self.type)
        self.rect.y = 360

    def update(self, game_speed, obstacles_list):
        self.move()

        if self.index >= self.wait+8:
            self.index = 0

        if self.move_state:
            self.obstacle_type = 1
            super().update(-game_speed, obstacles_list)
        else:
            self.obstacle_type = 0
            super().update(game_speed, obstacles_list)

    def move(self):
        self.index += 1

        if (self.index//self.wait) == 0:
            self.move_state = False
        else:
            self.move_state = True
