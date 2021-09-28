import pygame
import os

# Global Constants
TITLE = 'DIno Runner'
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
DEFAULT_NUMBER_OF_LIVES = 5

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
CHAINSAW_TYPE = "chainsaw"
SHURIKEN_TYPE = "shuriken"
SWORD_TYPE = "sword"
HALBERD_TYPE = "halberd"

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, 'DinoWallpaper.png'))
RESTART = pygame.image.load(os.path.join(IMG_DIR, 'Other/Reset.png'))

GAME_OVER_BLACK_IMAGE = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))
GAME_OVER_BLACK = pygame.transform.scale(GAME_OVER_BLACK_IMAGE, (600, 200))
GAME_OVER_WHITE_IMAGE = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOverWhite.png'))
GAME_OVER_WHITE = pygame.transform.scale(GAME_OVER_WHITE_IMAGE, (600, 200))
GAME_OVER = [GAME_OVER_BLACK, GAME_OVER_WHITE]

DINO_DEAD = pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoDead.png'))
DINO_DEAD_DUCK = pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoDuckDead.png'))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer1.png")),
]

RUNNING_CHAINSAW = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRunChainsaw1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRunChainsaw2.png")),
]

RUNNING_SHURIKEN = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Ninja.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Ninja.png")),
]

RUNNING_SWORD = [
    pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoRun1Sword.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoRun2Sword.png')),
]

RUNNING_HALBERD = [
    pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoRun1Halberd.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoRun2Halberd.png')),
]

RUNNING_HALBERD_KILL = [
    pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoRun1HalberdKill.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoRun2HalberdKill.png')),
]

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_CHAINSAW = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuckChainsaw1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuckChainsaw2.png")),
]

DUCKING_SHURIKEN = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Ninja.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Ninja.png")),
]

DUCKING_SWORD = [
    pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoDuck1Sword.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoDuck2Sword.png')),
]

DUCKING_HALBERD = [
    pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoDuck1Halberd.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoDuck2Halberd.png')),
]

DUCKING_HALBERD_KILL = [
    pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoDuckKill1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoDuckKill2.png')),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))
JUMPING_CHAINSAW = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpChainsaw.png"))
JUMPING_SHURIKEN = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpNinja.png"))
JUMPING_SWORD = pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoJump1Sword.png'))
JUMPING_HALBERD = pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoJump1Halberd.png'))
JUMPING_HALBERD_KILL = pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoRunKillHalberd.png'))

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

SNAKE = [
    pygame.image.load(os.path.join(IMG_DIR, "Snake/SnakeStill.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Snake/SnakeMove2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/Hammer.png'))
CHAINSAW = pygame.image.load(os.path.join(IMG_DIR, 'Other/Chainsaw.png'))
SHURIKEN = pygame.image.load(os.path.join(IMG_DIR, 'Other/Shuriken.png'))
SHURIKEN_RESIZED = pygame.transform.scale(SHURIKEN, (30, 30))
SWORD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Sword.png'))
SWORD_RESIZED = pygame.transform.scale(SWORD, (48, 48))
HALBERD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Halberd.png'))
HALBERD_RESIZED = pygame.transform.scale(HALBERD, (48, 48))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART_WHITE = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeartWhite.png'))
HEART_BLACK = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))
