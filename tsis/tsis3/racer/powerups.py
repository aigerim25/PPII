import pygame, sys 
from pygame.locals import*
import random, time
WHITE = (255,255,255)
BLACK = (0,0,0)
class Shield(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.active = False 
        self.timer = 0
        self.life_timer = 300
        self.image = pygame.image.load("shield.png").convert()
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
    def activate(self):
        self.active = True 
        self.timer = 300
    def move(self):
        self.rect.move_ip(0,5)
        if self.rect.top > 600 or self.life_timer <= 0:
            self.rect.center = (random.randint(40, 360), -100)
            self.life_timer = 300
    def update(self):
        if self.active:
            self.timer -= 1
            if self.timer <= 0:
                self.active = False          


class Nitro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.active = False
        self.timer = 0
        self.life_timer = 300
        self.image = pygame.image.load("nitro.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
    def activate(self):
        self.active = True
        self.timer = 180
    def move(self):
        self.rect.move_ip(0,5)
        if self.rect.top > 600 or self.life_timer <=0:
            self.rect.center = (random.randint(40, 360), -100)     
            self.life_timer = 300
    def update(self):
        if self.active:
            self.timer -= 1
            if self.timer <= 0:
                self.active = False           

             

        