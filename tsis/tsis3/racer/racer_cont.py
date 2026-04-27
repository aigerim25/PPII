import pygame, sys
from pygame.locals import*
import random, time
from powerups import Shield
from powerups import Nitro
from leaderboard import save_score, get_top_scores

pygame.init()
FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
speed = 5
score = 0
N = 5
slip = False 
slip_timer = 0
slip_direction = 0
current_speed = 0
lanes = [80, 160, 240, 320]

username = ""
entering_name = False

score_saved = False
distance = 0
finish_distance = 1000

screen_state = "menu"

enemies = pygame.sprite.Group()
bareer = pygame.sprite.Group()
oil = pygame.sprite.Group()
coins = pygame.sprite.Group()

pygame.display.set_caption("Game")
screen = pygame.display.set_mode((400, 600))
screen.fill(WHITE)
FramePerSec = pygame.time.Clock()

font = pygame.font.SysFont("Verdana", 60)
score_font = pygame.font.SysFont("Verdana", 20)
small_font = pygame.font.SysFont("Verdana",30) # для пользователя
top10_font = pygame.font.SysFont("Verdana", 18)
background = pygame.image.load("race1.png")
background = pygame.transform.scale(background, (400,600))

def safe_spawn(group, current_obj = None, miny = -1200, maxy = -100):
    for attempt in range(100):
        x = random.choice(lanes)
        y = random.randint(miny, maxy)

        ok = True
        for groups in group:
            for obj in groups:
                if obj == current_obj:
                    continue

                same_line = obj.rect.centerx == x 
                too_close_same_lane = abs(obj.rect.centery - y) < 220
                too_close_general = abs(obj.rect.centery -y ) < 80
                if (same_line and too_close_same_lane) or too_close_general:
                    ok = False
                    break 
            if not ok:
                break
        if ok:
            return x, y                

class Enemy (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png").convert()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image,(50,100))
        self.rect = self.image.get_rect()
        self.rect.center = safe_spawn([enemies, bareer, oil, coins])                      
    def move(self):
        self.rect.move_ip(0,current_speed)

        if self.rect.top > 600:
            self.rect.center = safe_spawn([enemies, bareer, oil, coins], self) 
      
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
        global slip, slip_timer, slip_direction, nitro
        
        if nitro.active:
            player_speed = 10
        else:
            player_speed = 5 

        pressed_keys = pygame.key.get_pressed()
        if slip:
            self.rect.move_ip(slip_direction, 0)
            slip_timer -= 1

            if slip_timer <= 0:
                slip = False
        else:
            if self.rect.left > 0 and pressed_keys[K_LEFT]:
                self.rect.move_ip(-player_speed,0)
            if self.rect.right < 400 and pressed_keys[K_RIGHT]:
                self.rect.move_ip(player_speed,0)   
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, 400)             
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
        self.rect.center = safe_spawn([enemies, bareer, oil, coins]) 
        

    def move(self):
        self.rect.move_ip(0,current_speed)
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
        self.rect = self.image.get_rect()
        self.rect.center = safe_spawn([enemies, bareer, oil, coins])         

class Oil(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("oil.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (120,70))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), -80)
    def move(self):
        self.rect.move_ip(0,current_speed) # объект идет вниз, это тоже координаты
        if self.rect.top > 600:
            self.rect.center = safe_spawn([enemies, bareer, oil, coins]) 

class Bareer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bareer.png").convert()
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (60,80))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,360), -150)
    def move(self):
        self.rect.move_ip(0, current_speed) # увеличиваем ускорения окружения
        if self.rect.top > 600:
            self.rect.center = safe_spawn([enemies, bareer, oil, coins])    
P1 = Player()
C1 = Coins()
O1 = Oil()
B1 = Bareer()
shield = Shield() # пришел нам из файла powerups
shield.rect.center = safe_spawn([enemies, bareer, oil, coins])

nitro = Nitro()
nitro.rect.center = safe_spawn([enemies, bareer, oil, coins])
oil.add(O1)

bareer.add(B1)

coins.add(C1)

# enemies.add(E1) --- создание одной машины
all_sprites = pygame.sprite.Group()
for i in range(4):
    enemy = Enemy()
    enemies.add(enemy)
    all_sprites.add(enemy)

game_over = False
speed_increased = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()  
        if screen_state == "menu": # MENU
            if event.type == KEYDOWN:
                if event.key == K_p:
                    screen_state = "game"
                    entering_name = True
                    username = ""
                    continue
                elif event.key == K_l:
                    screen_state = "leaderboard"
                elif event.key == K_q:
                    pygame.quit()
                    sys.exit()   
        if screen_state == "leaderboard": # LEADERBOARD
            if event.type == KEYDOWN:
                if event.key == K_b:
                    screen_state = "menu"            
        if screen_state == "game" and entering_name:
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    entering_name = False
                elif event.key == K_BACKSPACE:
                    username = username[:-1]
                elif event.unicode.isprintable():
                    username += event.unicode                                            
        if game_over: # restart
            if event.type == KEYDOWN and event.key == K_r:
                game_over = False 
                speed = 5
                score = 0 
                speed_increased = False 
                slip = True 
                slip_timer = 0
                slip_direction = 0
                shield.active = False 
                shield.timer = 0
                nitro.active = False
                nitro.timer = 0
                score_saved = False
                distance = 0
                C1.reset()
                P1.rect.center = (160, 520)
                O1.rect.center = safe_spawn([enemies, bareer, oil, coins], O1)
                B1.rect.center = safe_spawn([enemies, bareer, oil, coins], B1)
                nitro.rect.center = safe_spawn([enemies, bareer, oil, coins], nitro)
                shield.rect.center = safe_spawn([enemies, bareer, oil, coins], shield)
            elif event.type == KEYDOWN and event.key == K_m:
                screen_state = "menu"
                game_over = False
                entering_name = False
                username = ""
                score = 0
                distance = 0
                score_saved = False    

                for enemy in enemies:
                    enemy.rect.center = safe_spawn([enemies, bareer, oil, coins], enemy)
    if screen_state == "menu":
        screen.fill(BLACK)
        title = font.render("RACER", True, WHITE)
        play_text = score_font.render("Press P to Play", True, WHITE)
        leaderboard_text = score_font.render("Press L for leaderboard", True, WHITE)
        quit_text = score_font.render("Press Q to Quit", True, WHITE)

        screen.blit(title, (90, 120))
        screen.blit(play_text, (100, 250))
        screen.blit(leaderboard_text, (70, 300))
        screen.blit(quit_text, (100, 350))

        pygame.display.update()
        FramePerSec.tick(FPS)
        continue   
    if screen_state == "leaderboard":
        screen.fill(BLACK)

        title = small_font.render("TOP 10 SCORES", True, WHITE) 
        screen.blit(title, (80, 60))
        top_scores = get_top_scores()

        y = 120
        for i, item in enumerate(top_scores):
            line = score_font.render(str(i+1) + "." + item["name"] + " - " + str(item["score"]), True, WHITE)
            screen.blit(line, (80, y))
            y += 30
        back_text = score_font.render("Press B to back", True, WHITE)
        screen.blit(back_text, (100,520))
        pygame.display.update()
        FramePerSec.tick(FPS)
        continue                 
    if entering_name:
        screen.fill(BLACK)
        title = small_font.render("Enter your name:", True, WHITE)
        name_text = small_font.render(username, True, WHITE)
        screen.blit(title, (60, 180))
        screen.blit(name_text, (60, 250))

        pygame.display.update()
        FramePerSec.tick(FPS)
        continue                
    if not game_over:
        screen.blit(background, (0,0))
        for o in oil:
            o.move()
            screen.blit(o.image, o.rect)
        for c in coins:
            c.move()
            screen.blit(c.image, c.rect)
        for b in bareer:
            b.move()
            screen.blit(b.image, b.rect)
        for e in enemies:
            e.move()
            screen.blit(e.image, e.rect)

        shield.move()
        shield.update()
        screen.blit(shield.image, shield.rect)    

        nitro.move()
        nitro.update()
        screen.blit(nitro.image, nitro.rect)

        P1.update()
        screen.blit(P1.image, P1.rect)

        hit_enemy = pygame.sprite.spritecollideany(P1, enemies)
        hit_bareer = pygame.sprite.spritecollideany(P1, bareer)

        if hit_enemy or hit_bareer:
            if shield.active:
                shield.active = False

                if hit_enemy:
                    hit_enemy.rect.center = safe_spawn([enemies, bareer, oil, coins], hit_enemy)
                if hit_bareer:
                    hit_bareer.rect.center = safe_spawn([enemies,bareer, oil, coins], hit_bareer)    
            else:
                game_over = True        

        if nitro.active:
            current_speed = 10
        else:
            current_speed = speed    
        distance += current_speed * 0.1     
        if pygame.sprite.spritecollideany(P1, oil):
            if not slip:
                slip = True
                slip_timer = 25 
                slip_direction = random.choice([-3,3]) 

        collected_coin = pygame.sprite.spritecollideany(P1, coins)
        if collected_coin:
            score += collected_coin.weight * 10
            collected_coin.reset()
        if score >= 100 and not speed_increased:
            speed += 3
            speed_increased = True     
        if pygame.sprite.collide_rect(P1, shield): # как я поняла, pygame.sprite.collideany мы используем для группы, а щит используется у нас не всегда, как коинс или другие
            if not shield.active:
                shield.activate()
                shield.rect.center = (-100, -100)    
        if pygame.sprite.collide_rect(P1, nitro):
            if not nitro.active:
                nitro.activate()
                nitro.rect.center = (-100, -100)
        distance_text = score_font.render("Distance: " + str(int(distance)) + "/" + str(finish_distance), True, WHITE)        
        score_text = score_font.render("Coins: " + str(score), True, WHITE)
        screen.blit(score_text, (280, 10))    
        screen.blit(distance_text, (10, 70))

        if nitro.active:
            nitro_text = score_font.render("Nitro: " + str(nitro.timer // 60) + "s", True, WHITE)     
            screen.blit(nitro_text, (10,10))
        if shield.active:
            shield_text = score_font.render("Shield: " + str(shield.timer // 60) + "s", True, WHITE)          
            screen.blit(shield_text, (10,40))            
    else:
        if not score_saved:
            final_score = score + int(distance)
            save_score(username, final_score, int(distance))
            score_saved = True 

        screen.fill(RED)

        text = font.render("Game Over", True, WHITE)
        restart_text = pygame.font.SysFont("Verdana", 25).render("Press R to retry", True, WHITE)
        coins_text = score_font.render("Coins: " + str(score), True, WHITE)
        distance_text = score_font.render("Distance: " + str(int(distance)), True, WHITE)
        final_text = score_font.render("Final Score: " + str(score + int(distance)), True, WHITE)

        menu_text = score_font.render("Press M for Main Menu", True, WHITE)
        
        screen.blit(text, (40, 70))
        screen.blit(coins_text, (120, 180))
        screen.blit(distance_text, (120, 115))
        screen.blit(final_text, (120, 250))

        screen.blit(restart_text, (100, 330))
        screen.blit(menu_text, (80, 370))
    pygame.display.update()
    FramePerSec.tick(FPS)                                        