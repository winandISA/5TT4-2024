import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

print("test")
input("coucou")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Premier Jeu en Pygame")

background_img = pygame.image.load("resources/ciel.jpg")  # Fond d'écran
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

rocket_img = pygame.image.load("resources/fusee-de-dessin-anime-autocollant.gif")  # Remplace par le chemin de ton image
rocket_img = pygame.transform.scale(rocket_img, (50, 50))

target_img = pygame.image.load("resources/planet-earth-cartoon-style.gif")  # Remplace par le chemin de ton image
target_img = pygame.transform.scale(target_img, (50, 50))

player_pos = [50, 50]
player_size = 50
player_angle = 0

target_pos = [WIDTH - 100, HEIGHT - 100]
target_size = 50

speed = 5
clock = pygame.time.Clock()

target_rect = pygame.Rect(target_pos[0], target_pos[1], target_size, target_size)

continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= speed
        player_angle = 0
    if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - player_size:
        player_pos[1] += speed
        player_angle = 180
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= speed
        player_angle = 90
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += speed
        player_angle = -90

    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)

    if player_rect.colliderect(target_rect):
        print("Bravo ! Vous avez gagné !")
        continuer = False

    screen.blit(background_img, (0, 0))

    rotated_rocket = pygame.transform.rotate(rocket_img, player_angle)
    rocket_rect = rotated_rocket.get_rect(center=(player_pos[0] + player_size // 2, player_pos[1] + player_size // 2))
    screen.blit(rotated_rocket, rocket_rect.topleft)

    screen.blit(target_img, target_pos)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
sys.exit()
