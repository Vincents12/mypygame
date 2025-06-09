import pygame #import pygame
import time
import random

pygame.init() #initialize a pygame classes

#set pygame resolution
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))

# background

background_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))


# picture
picture = pygame.image.load("cat.png")
picture = pygame.transform.scale(picture,(220,120))
picture_rect = picture.get_rect()
picture_speed = [13,13]

picture1 = pygame.image.load("othercat.png")
picture1 = pygame.transform.scale(picture1,(220,120))
picture_rect1 = picture1.get_rect()
picture_rect1.x = 500  # Move the second picture to the right
picture_rect1.y = 300  # Move the second picture down
picture_speed1 = [30,30]


#let's it run
running = True


while running: 
    for event in pygame.event.get(): #when something happens in the game
        
        if event.type == pygame.QUIT: #when pressing the X 
            running = False #actually quits the game and doesn't let it crash
    screen.fill(background_colour)

    # Change background color every frame
    background_colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    screen.fill(background_colour)
    screen.blit(picture, picture_rect)
    screen.blit(picture1, picture_rect1)

    # Move pictures
    picture_rect = picture_rect.move(picture_speed)
    picture_rect1 = picture_rect1.move(picture_speed1)

    # Bounce off walls
    if picture_rect.left < 0 or picture_rect.right > width:
        picture_speed[0] = -picture_speed[0]
    if picture_rect.top < 0 or picture_rect.bottom > height:
        picture_speed[1] = -picture_speed[1]

    if picture_rect1.left < 0 or picture_rect1.right > width:
        picture_speed1[0] = -picture_speed1[0]
    if picture_rect1.top < 0 or picture_rect1.bottom > height:
        picture_speed1[1] = -picture_speed1[1]

    # Bounce off each other
    if picture_rect.colliderect(picture_rect1):
        picture_speed[0] = -picture_speed[0]
        picture_speed[1] = -picture_speed[1]
        picture_speed1[0] = -picture_speed1[0]
        picture_speed1[1] = -picture_speed1[1]

    pygame.display.flip()
    time.sleep(10/1000)

pygame.quit()

