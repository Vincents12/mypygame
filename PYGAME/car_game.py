import pygame
from car import Car

pygame.init()

width, height = 400, 400
screen = pygame.display.set_mode((width, height))

GREEN = (100, 255, 200)
GREY = (210, 210,210)
WHITE = (255,255,255)
RED = (255,0,0)
PURPLE = (255,0,255)

all_sprite_list = pygame.sprite.Group()
PlayerCar1 = Car(RED,20,30)
PlayerCar1.rect.x = 200
PlayerCar1.rect.y = 300

PlayerCar2 = Car(PURPLE,20,30)
PlayerCar2.rect.x = 100
PlayerCar2.rect.y = 100

all_sprite_list.add(PlayerCar1)
all_sprite_list.add(PlayerCar2)


running = True
while running: 
    for event in pygame.event.get(): 
        
        if event.type == pygame.QUIT: 
            running = False 
    all_sprite_list.update()
    all_sprite_list.draw(screen)
    
    
    pygame.display.flip()

pygame.quit()