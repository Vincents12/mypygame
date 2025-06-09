import pygame

#Let's import the car class
from car import Car

pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height))

GREEN = (100, 255, 200)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

#Create a list that will contain all our sprites
all_sprite_list = pygame.sprite.Group()
playerCar1 = Car(RED, 20, 30)
playerCar1.rect.x = 200
playerCar1.rect.y = 300

playerCar2 = Car(PURPLE, 20, 30)
playerCar2.rect.x = 100
playerCar2.rect.y = 100

#Add our sprites to the list
all_sprite_list.add(playerCar1)
all_sprite_list.add(playerCar2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill(GREEN)
    collide = playerCar1.rect.colliderect(playerCar2)
    if collide:
         playerCar1.rect.x = 200
         playerCar1.rect.y = 300
         playerCar2.rect.x = 100
         playerCar2.rect.y = 100
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerCar1.moveLeft(1)
        if keys [pygame.K_RIGHT]:
            playerCar1.moveRight(1,width)
        if keys[pygame.K_DOWN]:
            playerCar1.moveDown(1)
        if keys [pygame.K_UP]:
            playerCar1.moveUp(1)

        if keys[pygame.K_a]:
                playerCar2.moveLeft(1)
        if keys [pygame.K_d]:
            playerCar2.moveRight(1,width)
        if keys[pygame.K_s]:
            playerCar2.moveDown(1)
        if keys [pygame.K_w]:
            playerCar2.moveUp(1)
    screen.fill (GREEN)
    pygame.draw.rect(screen, GREY, [40,0,200,500])
    pygame.draw.line(screen, WHITE, [140,0],[140,500], 5)



    #Draw all our sprites
    all_sprite_list.update()
    all_sprite_list.draw(screen)

    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(60)

pygame.quit()