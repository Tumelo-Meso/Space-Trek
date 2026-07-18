import pygame
pygame.font.init()

#Game configuration settings 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FPS = 60
FONT = pygame.font.SysFont("Arial", 30)
GAME_OVER_FONT = pygame.font.SysFont("Arial", 72)
INFO_FONT = pygame.font.SysFont("Arial", 36)
clock = pygame.time.Clock()

BG = pygame.image.load("images/star.png")
BG = pygame.transform.scale(BG,(SCREEN_WIDTH,SCREEN_HEIGHT))

#Player Setting configuration 
PLAYER_VEL = 6.5
PLAYER_WIDTH = 120
PLAYER_HEIGHT = 120
PLAYER_SHIP = pygame.image.load("images/ship.png")
PLAYER_SHIP = pygame.transform.scale(PLAYER_SHIP, (PLAYER_WIDTH,PLAYER_HEIGHT))

ENEMY_SHIP = pygame.image.load("images/e-ship.png")
ENEMY_WIDTH = 60
ENEMY_HEIGHT = 60
ENEMY_SHIP = pygame.transform.scale(ENEMY_SHIP,(ENEMY_WIDTH,ENEMY_HEIGHT))
ENEMY_SHIP_VEL = 0.5

BULLET = pygame.image.load("images/bullet.png")
BULLET = pygame.transform.scale(BULLET,(30,30))
BULLET_VEL = 15.5


EXPLOSION = pygame.image.load("images/explosion.png")
EXPLOSION = pygame.transform.scale(EXPLOSION,(ENEMY_WIDTH+25,ENEMY_HEIGHT+25))