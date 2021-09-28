import pygame

from nlc_dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT


FONT_STYLE = 'freesansbold.ttf'
black_color = (0, 0, 0)
white_color = (255, 255, 255)


def get_score_element(points, black):
    font = pygame.font.Font(FONT_STYLE, 22)

    if not black:
        text = font.render('Score: ' + str(points), True, black_color)
    else:
        text = font.render('Score: ' + str(points), True, white_color)

    text_rect = text.get_rect()
    text_rect.center = (1000, 50)

    return text, text_rect


def get_max_score_element(max_points, black):
    font = pygame.font.Font(FONT_STYLE, 22)

    if not black:
        text = font.render('Max Score: ' + str(max_points), True, black_color)
    else:
        text = font.render('Max Score: ' + str(max_points), True, white_color)

    text_rect = text.get_rect()
    text_rect.center = (1000, 75)

    return text, text_rect


def get_level_element(level, black):
    font = pygame.font.Font(FONT_STYLE, 22)

    if not black:
        text = font.render('Level: ' + str(level), True, black_color)
    else:
        text = font.render('Level: ' + str(level), True, white_color)

    text_rect = text.get_rect()
    text_rect.center = (1000, 100)

    return text, text_rect


def get_max_level_element(max_level, black):
    font = pygame.font.Font(FONT_STYLE, 22)

    if not black:
        text = font.render('Max Level: ' + str(max_level), True, black_color)
    else:
        text = font.render('Max Level: ' + str(max_level), True, white_color)

    text_rect = text.get_rect()
    text_rect.center = (1000, 125)

    return text, text_rect


def get_centered_message(message, width=SCREEN_WIDTH // 2, height=SCREEN_HEIGHT // 2):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(message, True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)

    return text, text_rect
