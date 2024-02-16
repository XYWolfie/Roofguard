import pygame
import pygame.freetype
import os
from random import choice, randint
from itertools import cycle
vec = pygame.math.Vector2
pygame.init()


screen = pygame.display.set_mode((800, 600))



RESOLUTION = 800, 600
FPS = 60
PLAYER_SPEED = 400
FALLING_SPEED = 200
ANIM_THRESHOLD = 0.05

black = (0, 0, 0)
red = (73, 12, 15)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((800/2),(500/2))
    screen.blit(TextSurf, TextRect)

playerimg = pygame.image.load("roofguard.png")
playerimg = pygame.transform.scale(playerimg, (86, 30))

carimg = pygame.image.load("car.png")
carimg = pygame.transform.scale(carimg, (345, 120))

carimg2 = pygame.image.load("car.png")
carimg2 = pygame.transform.scale(carimg, (345, 120))

carimg3 = pygame.image.load("car.png")
carimg3 = pygame.transform.scale(carimg, (345, 120))

b_carimg = pygame.image.load("burning_car.png")
b_carimg = pygame.transform.scale(b_carimg, (345, 245))

tile = pygame.image.load("tile.png")
tile = pygame.transform.scale(tile, (80, 100))

broken = False
hit = 0
howmany = 0


bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (800, 600))

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, falling_stuff, *grps):
        super().__init__(*grps)

        self.images = []

        self.img = pygame.image.load(os.path.join('roofguard.png')).convert()
        self.images.append(self.img)
        self.image = self.images[0]

        screen =pygame.display.set_mode((800, 500))
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
        self.pressed = pygame.key.get_pressed()
        if self.pressed[pygame.K_a]: d -= 1
        if self.pressed[pygame.K_d]: d += 1

        self.rect.move_ip(d * dt *PLAYER_SPEED, 0)
        self.display_rect = pygame.display.get_surface().get_rect()
        self.rect.clamp_ip(self.display_rect)

       

        for self.stuff in self.falling_stuff:
            if self.hitbox.colliderect(self.stuff.rect):
                self.stuff.kill()
                self.score += 1

        self.hitbox.center = self.rect.center
        self.hitbox.move_ip(5 if self.direction == 'LEFT' else 10, 10)

        pygame.display.update()
        
    
class Tiles(pygame.sprite.Sprite):
    def __init__(self, pos, *grps):
        pygame.sprite.Sprite.__init__(self)
        self.image = tile
        self.rect = self.image.get_rect() # henter self.image sin størrelse og lager en hitbox
        self.pos = vec(1200,randint(300,950))
        self.rect.center = self.pos
        self.speed = 300

    def update(self, dt, events):
            self.rect.move_ip(0, FALLING_SPEED * dt)
            self.display_rect = pygame.display.get_surface().get_rect()
            broken == False
            self.hit = 0
            if self.rect.top > 500:
                
                self.kill()
                self.hit = hit + 1
                broken == True
                screen.blit(b_carimg, (-150,340))
                
                print ("meow")
                self.font = pygame.freetype.SysFont('comic sans', 80)
                self.font.render_to(screen, (100, 250), f'GAME OVER', 'red')
        
                pygame.display.update()

                pygame.time.wait(5000)
                self.end()
        
             
   

class Car1(pygame.sprite.Sprite):
    def __init__(self, game, pos, *grps):
        super().__init__(*grps)
        self.groups = game.all_sprites
        self.game = game

        self.images = [carimg, b_carimg]
        
        self.burning = False

        self.burning = [b_carimg]

    def update(self):  
        if broken == True:
            self.burning = True
            self.images = [1]
            print ("woof")

    def animate(self):
        now = pygame.time.get_ticks()

        if self.burning:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.burning)
                self.image = self.burning[self.current_frame]




    



