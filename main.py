import pygame
import pygame.freetype
import os
from random import choice, randint
from itertools import cycle
from pygame import mixer
from sprites import *
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Roofguard")


RESOLUTION = 800, 600
FPS = 10
TILESIZE = 32
PLAYER_SPEED = 400
FALLING_SPEED = 200
ANIM_THRESHOLD = 0.05

black = (0, 0, 0)
red = (73, 12, 15)

txt = pygame.freetype.Font("prstart.ttf", 34)
game_over_text = txt.render("Game over, click R to restart", False, ('red'))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('prstart.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((800/2),(600/2))
    screen.blit(TextSurf, TextRect)

playerimg = pygame.image.load("roofguard.png")
playerimg = pygame.transform.scale(playerimg, (130, 24))

carimg = pygame.image.load("car.png")
carimg = pygame.transform.scale(carimg, (345, 120))

carimg2 = pygame.image.load("car.png")
carimg2 = pygame.transform.scale(carimg, (345, 120))

carimg3 = pygame.image.load("car.png")
carimg3 = pygame.transform.scale(carimg, (345, 120))

b_carimg = pygame.image.load("burning_car.png")
b_carimg = pygame.transform.scale(b_carimg, (345, 245))

tileimg = pygame.image.load("tile.png")
tileimg = pygame.transform.scale(tileimg, (45, 80))

broken = False
hit = 0
howmany = 0

game_state = "start_menu"

bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (800, 600))

def draw_start_menu():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('Roofguard', True, (255, 255, 255))
    start_button = font.render("press 'space' to start", True, (255, 255, 255))
    screen.blit(title, (800/2 - title.get_width()/2, 600/2 - title.get_height()/2))
    screen.blit(start_button, (800/2 - start_button.get_width()/2, 600/2 + start_button.get_height()/2))
    pygame.display.update()

def draw_game_over_screen():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    restart_button = font.render('R - Restart', True, (255, 255, 255))
    quit_button = font.render('Q - Quit', True, (255, 255, 255))
    screen.blit(restart_button, (800/2 - restart_button.get_width()/2, 600/1.9 + restart_button.get_height()))
    screen.blit(quit_button, (800/2 - quit_button.get_width()/2, 600/2 + quit_button.get_height()/2))
    pygame.display.update()


while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           quit()
   if game_state == "start_menu":
       draw_start_menu()
       keys = pygame.key.get_pressed()
       if- keys[pygame.K_SPACE]:
           player_x = 200
           player_y = 400
           game_state = "game"
           game_over = False

   elif game_state == "game_over":
       draw_game_over_screen()
       keys = pygame.key.get_pressed()
       if keys[pygame.K_r]:
           game_state = "start_menu"
       if keys[pygame.K_q]:
           pygame.quit()
           quit()
  
   elif game_state == "game":
       
    class Player(pygame.sprite.Sprite):
        def __init__(self, pos, falling_stuff, *grps):
            super().__init__(*grps)

            self.images = []

            img = pygame.image.load(os.path.join('roofguard.png')).convert()
            self.images.append(img)
            self.image = self.images[0]

            self.screen =pygame.display.set_mode((800, 600))
            pygame.display.update()
            self.image = playerimg
            self.direction = "LEFT"
            self.animation_counter = 0
            self.rect = self.image.get_rect(topleft=pos)
            self.falling_stuff = falling_stuff
            self.score = 0
            self.hitbox = pygame.Rect(0, 0, 130, 40)
            self.hitbox.center = self.rect.center
            self.hitbox.move_ip(-10, -10)


        
        def update(self, dt, events):
            d = 0
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_a]: d -= 1
            if pressed[pygame.K_d]: d += 1
            global FALLING_SPEED
            global PLAYER_SPEED
                

            self.rect.move_ip(d * dt * PLAYER_SPEED, 0)
            display_rect = pygame.display.get_surface().get_rect()
            self.rect.clamp_ip(display_rect)
        

            for stuff in self.falling_stuff:
                if self.hitbox.colliderect(stuff.rect):
                    stuff.kill()
                    self.score += 1

                    if self.score >= 5:
                        PLAYER_SPEED = 450
                        FALLING_SPEED = 250
                    if self.score >= 10:
                        PLAYER_SPEED = 500
                        FALLING_SPEED = 300
                    if self.score >= 15:
                        PLAYER_SPEED = 550
                        FALLING_SPEED = 350
                    if self.score >= 20:
                        PLAYER_SPEED = 600
                        FALLING_SPEED = 400
                    if self.score >= 25:
                        PLAYER_SPEED = 650
                        FALLING_SPEED = 450
                    if self.score >= 30:
                        PLAYER_SPEED = 700
                        FALLING_SPEED = 500
                    if self.score >= 35:
                        PLAYER_SPEED = 750
                        FALLING_SPEED = 550
                    if self.score >= 40:
                        PLAYER_SPEED = 800
                        FALLING_SPEED = 600
                    if self.score >= 45:
                        PLAYER_SPEED = 850
                        FALLING_SPEED = 650
                    if self.score >= 50:
                        PLAYER_SPEED = 900
                        FALLING_SPEED = 700
                    if self.score >= 55:
                        PLAYER_SPEED = 950
                        FALLING_SPEED = 750
                    if self.score >= 60:
                        PLAYER_SPEED = 1000
                        FALLING_SPEED = 800

            self.hitbox.center = self.rect.center
            self.hitbox.move_ip(5 if self.direction == 'LEFT' else 10, 10)

            pygame.display.update()
                
            

    class FallingStuff(pygame.sprite.Sprite):
            def __init__(self, pos, *grps):
                super().__init__(*grps)
                self.image = tileimg
                self.rect = self.image.get_rect(topleft=pos)
                

                
            def update(self, dt, events):
                global display_rect
                self.rect.move_ip(0, FALLING_SPEED * dt)
                display_rect = pygame.display.get_surface().get_rect()
                broken == False
                hit = 0
                global game_over
                global game_state

                if self.rect.top > 500:
                    if self.rect.left < 200:
                        self.kill()
                        hit = hit + 1
                        broken == True
                        screen.blit(b_carimg, (-150,340))
                        
                    
                        font = pygame.freetype.Font("prstart.ttf", 64)
                        font.render_to(screen, (100, 250), f'GAME OVER', 'red')
                
                        pygame.display.update()
                        pygame.time.wait (5000)
                        
                        game_over = True
                        game_state = "game_over"
                        main()

                        

                    if self.rect.left > 600:
                        self.kill()
                        hit = hit + 1
                        broken == True
                        screen.blit(b_carimg, (580,340))
                        
                        
                        font = pygame.freetype.Font("prstart.ttf", 64)
                        font.render_to(screen, (100, 250), f'GAME OVER', 'red')
                
                        pygame.display.update()
                        pygame.time.wait (5000)

                        game_over = True
                        game_state = "game_over"
                        main()
                  

                    else:
                        self.kill()
                        hit = hit + 1
                        broken == True
                        screen.blit(b_carimg, (215,340))
                        
                    
                        font = pygame.freetype.Font("prstart.ttf", 64)
                        font.render_to(screen, (100, 250), f'GAME OVER', 'red')
                
                        pygame.display.update()
                        pygame.time.wait (5000)
                        
                        game_over = True
                        game_state = "game_over"
                        main()



    def main():

            pygame.init()
            global game_state
            global font
            screen = pygame.display.set_mode(RESOLUTION)          
            if game_state == ("game"):
                dt, clock = 0, pygame.time.Clock()
                sprites = pygame.sprite.Group()
                falling_stuff = pygame.sprite.Group()
                player = Player((300, 360), falling_stuff, sprites)
                
                font = pygame.freetype.SysFont('txt', 40)

                CREATE_STUFF = pygame.USEREVENT + 1
                pygame.time.set_timer(CREATE_STUFF, randint(1000, 2000), True)
                while True:
                    events = pygame.event.get()
                    for e in events:
                        if e.type == pygame.QUIT:
                            return
                        if e.type == CREATE_STUFF:
                            pygame.time.set_timer(CREATE_STUFF, randint(1000, 2000), True)
                            FallingStuff((randint(50, 750), -TILESIZE), falling_stuff, sprites)
                    
                    screen.fill(black)
                    screen.blit(bg, (0, 0))
                    txt.render_to(screen, (20, 20), f'Score: {player.score}', 'black')
                    sprites.draw(screen)
                    screen.blit(carimg, (-150,465))
                    screen.blit(carimg2, (215,465))
                    screen.blit(carimg3, (580,465))
                    sprites.update(dt, events)
                    pygame.display.flip()
                    dt = clock.tick(FPS) / 1000

                    pygame.display.update()
                
                
            if game_state == "start_menu":
                draw_start_menu()
            if game_state == "game_over":
                draw_game_over_screen()
                pygame.display.update()
                    

            if game_state == "start_menu":
                global player_x
                global player_y
                global game_over
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    game_state = "game"
                    player_x = 200
                    player_y = 400
                    game_state = "game"
                    game_over = False

            if game_state == "game_over":
                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:
                    game_state = "start_menu"
                if keys[pygame.K_q]:
                    pygame.quit()
                    quit()

    

    if __name__ == "__main__":
        main()
  
   elif game_over:
       game_state = "game_over"
       game_over = False

                

