import pygame
WHITE = (255,255,255)

class Car(pygame.sprite.Sprite):

    def __init__(self, colour, width, height):
        #Call Sprite constructor
        super().__init__()

        #Set the background colour and set it to be transparent
        self.image = pygame.Surface([width,height]) #Create out pygame surface
        self.image.fill(WHITE) #Fill that surface with a colour
        self.image.set_colorkey(WHITE)

        #Draw a rectangle
        pygame.draw.rect(self.image, colour, [0, 0, width, height])
        # Instead we could load a proper pciture of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()
        self.rect = self.image.get_rect()
    def moveRight(self, pixels, max_x):
        new_x = self.rect.x + pixels
        if new_x >= max_x:
            self.rect.x = max_x - 10
        else:
            self.rect.x = new_x
    def moveLeft(self,pixels):
        self.rect.x -= pixels
    
    def moveDown(self, pixels):
        self.rect.y += pixels

    def moveUp(self, pixels):
        self.rect.y -= pixels