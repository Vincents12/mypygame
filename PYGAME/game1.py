import pygame

pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height))

rect_colour = 10,120,120
circle_colour = 200,10,10
line_colour = 10,200,10
poly_colour = 50,50,50


running = True
while running: 
    for event in pygame.event.get(): 
        
        if event.type == pygame.QUIT: 
            running = False
    pygame.draw.rect(screen, rect_colour, pygame.Rect(30,20,60,60))
    pygame.draw.circle(screen, circle_colour,(200,200),20)
    pygame.draw.line(screen,line_colour,(300,200),(300,300),5)
    pygame.draw.polygon(screen,poly_colour,((200,200),(320,230),(20,10),(70,30),(100,130)))
    
    
    pygame.display.flip()


pygame.quit()