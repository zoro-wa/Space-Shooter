import pygame
from os.path import join
from random import randint


#setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surf = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Space-Shooter')
running = True
clock = pygame.time.Clock()

#plain surf
surf = pygame.Surface((100,200))
surf.fill('darkolivegreen2')
x = 100

#import an image
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2 , WINDOW_HEIGHT / 2))
player_direction = pygame.math.Vector2(2, -1)
player_speed = 10

star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(randint(0,WINDOW_WIDTH),randint(0,WINDOW_HEIGHT)) for i in range(20)]


meteor_surf = pygame.image.load(join('images', 'meteor.png'))
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load(join('images', 'laser.png'))
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))

while running:
    clock.tick(10)
    #event loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw the game
    display_surf.fill('azure3')
    for pos in star_positions:
       display_surf.blit(star_surf,pos)

    display_surf.blit(meteor_surf,meteor_rect)
    display_surf.blit(laser_surf,laser_rect)
    #player movement
    player_rect.center += player_direction * player_speed
    display_surf.blit(player_surf,player_rect.topleft)

    pygame.display.update()

pygame.quit()