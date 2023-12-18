import pygame
import sys

pygame.init()

#Game constants.
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (50, 50, 50)
PLAYER_COLOR = (255, 0, 0)
PLAYER_SIZE = 50
GRAVITY = 0.5
JUMP_STRENGTH = 10

#Display Setup.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Side Shooter")
