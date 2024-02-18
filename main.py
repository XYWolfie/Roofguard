import pygame
import pygame.freetype
import os
from random import choice, randint
from itertools import cycle
from pygame import mixer
from sprites import *
pygame.init()

screen = pygame.display.set_mode((800, 600))



RESOLUTION = 800, 600
FPS = 10
TILESIZE = 32
PLAYER_SPEED = 400
FALLING_SPEED = 250
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
    title = font.render('My Game', True, (255, 255, 255))
    start_button = font.render('Start', True, (255, 255, 255))
    screen.blit(title, (800/2 - title.get_width()/2, 600/2 - title.get_height()/2))
    screen.blit(start_button, (800/2 - start_button.get_width()/2, 600/2 + start_button.get_height()/2))
    pygame.display.update()

def draw_game_over_screen():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('Game Over', True, (255, 255, 255))
    restart_button = font.render('R - Restart', True, (255, 255, 255))
    quit_button = font.render('Q - Quit', True, (255, 255, 255))
    screen.blit(title, (800/2 - title.get_width()/2, 600/2 - title.get_height()/3))
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

            self.rect.move_ip(d * dt * PLAYER_SPEED, 0)
            display_rect = pygame.display.get_surface().get_rect()
            self.rect.clamp_ip(display_rect)

            

            for stuff in self.falling_stuff:
                if self.hitbox.colliderect(stuff.rect):
                    stuff.kill()
                    self.score += 1

                    if self.score >= 3:
                        PLAYER_SPEED == 600
                        FALLING_SPEED == 400

            self.hitbox.center = self.rect.center
            self.hitbox.move_ip(5 if self.direction == 'LEFT' else 10, 10)

            pygame.display.update()
                
            

    class FallingStuff(pygame.sprite.Sprite):
            def __init__(self, pos, *grps):
                super().__init__(*grps)
                self.image = tileimg
                self.rect = self.image.get_rect(topleft=pos)

                
            def update(self, dt, events):
                self.rect.move_ip(0, FALLING_SPEED * dt)
                display_rect = pygame.display.get_surface().get_rect()
                broken == False
                hit = 0
                if self.rect.top > 500:
                    if self.rect.left < 200:
                        self.kill()
                        hit = hit + 1
                        broken == True
                        screen.blit(b_carimg, (-150,340))
                        
                    
                        font = pygame.freetype.Font("prstart.ttf", 64)
                        font.render_to(screen, (150, 250), f'GAME OVER', 'red')
                
                        pygame.display.update()

                        pygame.time.wait(5000)
                        game_over == True
                        

                    if self.rect.left > 600:
                        self.kill()
                        hit = hit + 1
                        broken == True
                        screen.blit(b_carimg, (580,340))
                        
                        
                        font = pygame.freetype.Font("prstart.ttf", 64)
                        font.render_to(screen, (100, 250), f'GAME OVER', 'red')
                
                        pygame.display.update()

                        pygame.time.wait(5000)
                        game_over == True
                         
                    else:
                        self.kill()
                        hit = hit + 1
                        broken == True
                        screen.blit(b_carimg, (215,340))
                        
                    
                        font = pygame.freetype.Font("prstart.ttf", 64)
                        font.render_to(screen, (100, 250), f'GAME OVER', 'red')
                
                        pygame.display.update()

                        pygame.time.wait(5000)
                        game_over == True


    def main():

            pygame.init()
            screen = pygame.display.set_mode(RESOLUTION)

            

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
                
                

            
                            

    if __name__ == "__main__":
        main()
  
   elif game_over:
       game_state = "game_over"
       game_over = False


