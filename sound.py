import pygame

pygame.mixer.init()


laser_sound = pygame.mixer.Sound("sounds/laser.wav")

explosion_sound = pygame.mixer.Sound("sounds/explosion.wav")
engine_sound = pygame.mixer.Sound("sounds/engine.wav")
game_over_sound = pygame.mixer.Sound("sounds/game_over.wav")


laser_sound.set_volume(0.7)
explosion_sound.set_volume(0.50)
engine_sound.set_volume(0.4)
game_over_sound.set_volume(0.66)