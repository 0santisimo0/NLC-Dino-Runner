from nlc_dino_runner.utils.constants import HEART_BLACK, HEART_WHITE


class Live:
    POS_LIVES_Y = 30

    def __init__(self, pos_lives_x):
        self.image = HEART_WHITE
        self.rect = self.image.get_rect()
        self.rect.x = pos_lives_x
        self.rect.y = self.POS_LIVES_Y

    def draw(self, screen, black):
        if black:
            screen.blit(self.image, self.rect)
        else:
            self.image = HEART_BLACK
            screen.blit(self.image, self.rect)
