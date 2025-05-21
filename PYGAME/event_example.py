import pygame #import pygame
pygame.init() #initialize a pygame classes
import time
#set pygame resolution
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
background_colour = (255,0,0)

# picture
picture = pygame.image.load("cat.png")
picture = pygame.transform.scale(picture,(90,50))
picture_rect = picture.get_rect()


crosshair = pygame.image.load("crosshair.png")
crosshair = pygame.transform.scale(crosshair,(30,30))
crosshair_rect = crosshair.get_rect()
pos = [200,200]


#let's it run
running = True
while running: 
    for event in pygame.event.get(): 
        
        if event.type == pygame.QUIT: 
            running = False 
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pos = (crosshair_rect.center[0]-5,crosshair_rect.center[1])
            if event.key == pygame.K_RIGHT:
                pos = (crosshair_rect.center[0]+5,crosshair_rect.center[1])
            if event.key == pygame.K_DOWN:
                pos = (crosshair_rect.center[0],crosshair_rect.center[1]-5)
            if event.key == pygame.K_UP:
                pos = (crosshair_rect.center[0],crosshair_rect.center[1]+5)

    screen.fill(background_colour)
    screen.blit(picture, picture_rect)
    crosshair_rect.center = pos
    screen.blit(crosshair,crosshair_rect)
    
    
    pygame.display.flip()

pygame.quit()





""""""""""
    picture_rect = picture_rect.move(picture_speed)
    
    if picture_rect.left < 0 or picture_rect.right > width:
        picture_speed[0] = -picture_speed[0]
    if picture_rect.top < 0 or picture_rect.bottom > height:
        picture_speed[1] = -picture_speed[1]
time.sleep(10/1000)
        
"""""""""
