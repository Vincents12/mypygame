import pygame

class Car(pygame.sprite.Sprite):
    def __init__(self, colour, width, height):
        super().__init__


        self.image = pygame.surface((width,height))
        self.image.fill(255, 255,255)
        self.image.set_colorkey(255,255,255)

        pygame.draw.rect(self.image, colour, [0,0,width,height])
        self.rect = self.image.get_rect()

