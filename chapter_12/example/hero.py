import pygame

class Hero():

    def __init__(self,screen):
        self.screen = screen
        # image and react
        self.image = pygame.image.load('photos/hero.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # new hero
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image,self.rect)
