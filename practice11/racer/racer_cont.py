import pygame, sys
from pygame.locals import*
import random, time

pygame.init()
FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
speed = 5
score = 0
N = 5

pygame.display.set_caption("Game")
screen = pygame.display.set_mode((400, 600))
screen.fill(WHITE)
FramePerSec = pygame.time.Clock()

font = pygame.font.SysFont("Verdana", 60)
score_font = pygame.font.SysFont("Verdana", 20)
background = pygame.image.load("race1.png")
background = pygame.transform.scale(background, (400,600))

class Enemy (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png").convert()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image,(50,100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), 0)


    def move(self):
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), -50)
      

    def draw(self, surface):
        surface.blit(self.image, self.rect)        

class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image,(50,100))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < 400:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)        
    def draw(self,surface):
        surface.blit(self.image, self.rect)   

class Coins (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight = random.choice([1,2,3])
        self.image = pygame.image.load("coins.png").convert()
        self.image.set_colorkey(WHITE)
        if self.weight == 1:
            size = (20,20)
        elif self.weight == 2:
            size = (30,30)
        else:
            size = (40,40)        
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), -50)

    def move(self):
        self.rect.move_ip(0,5)
        if self.rect.top > 600:
            self.reset()

    def reset(self):
        self.weight = random.choice([1,2,3])
        if self.weight == 1:
            size = (20,20)
        elif self.weight == 2:
            size = (30,30)
        else:
            size = (40,40)   
        self.image = pygame.transform.scale(pygame.image.load("coins.png").convert(), size)
        self.image.set_colorkey(WHITE)    
        self.rect.center = (random.randint(40,360), -50)         

P1 = Player()
E1 = Enemy()
C1 = Coins()

coins = pygame.sprite.Group()
coins.add(C1)
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

game_over = False
speed_increased = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()  
        if game_over:
            if event.type == KEYDOWN and event.key == K_r:
                game_over = False 
                speed = 5
                score = 0 
                speed_increased = False 
                C1.rect.center = (random.randint(40,360), -50)
                P1.rect.center = (160, 520)

                for enemy in enemies:
                    enemy.rect.midbottom = (random.randint(40, 360), -100)
    if not game_over:
        screen.blit(background, (0,0))
        for entity in all_sprites:
            if isinstance(entity, Player):
                entity.update()
            else:
                entity.move()

            screen.blit(entity.image, entity.rect)
        if pygame.sprite.spritecollideany(P1, enemies):
            game_over = True
        collected_coin = pygame.sprite.spritecollideany(P1, coins)
        if collected_coin:
            score += collected_coin.weight * 10
            collected_coin.reset()

            if score >= 100 and not speed_increased:
                speed += 3
                speed_increased = True  
    else:
        screen.fill(RED)

        text = font.render("Game Over", True, WHITE)
        restart_text = pygame.font.SysFont("Verdana", 25).render("Press R to restart", True, WHITE)
        score_text = score_font.render("Coins: " + str(score), True, WHITE)

        screen.blit(text, (40, 200))
        screen.blit(restart_text, (80, 300))
        screen.blit(score_text, (280, 10))

    pygame.display.update()
    FramePerSec.tick(FPS)                                        
