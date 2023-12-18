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

#Player properties.
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - PLAYER_SIZE
player_speed = 5
player_jump = False
player_velocity_y = 0

#Game loop
running = True
while running:
    screen.fill(BG_COLOR)

#Event handling.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False

#Player movement.
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    player_x -= player_speed
if keys[pygame.K_RIGHT]:
    player_x += player_speed

# Player jump logic
if not player_jump:
    if keys[pygame.K_SPACE]:
        player_jump = True
        player_velocity_y = -JUMP_STRENGTH
else:
    player_velocity_y += GRAVITY
    player_y += player_velocity_y
    if player_y >= SCREEN_HEIGHT - PLAYER_SIZE:
        player_y = SCREEN_HEIGHT - PLAYER_SIZE
        player_jump = False

# Draw the player
pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y,
                                         PLAYER_SIZE, PLAYER_SIZE))

pygame.display.flip()

# Cap the frame rate
pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()