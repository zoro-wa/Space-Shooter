import pygame

from os.path import join


#setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surf = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Space-Shooter')
running = True

#plain surf
surf = pygame.Surface((100,200))
surf.fill('darkolivegreen2')
x = 100

#import an image
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()

while running:
    #event loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw the game
    display_surf.fill('azure3')
    x += 0.1
    display_surf.blit(player_surf,(x,150))
    pygame.display.update()
pygame.quit()