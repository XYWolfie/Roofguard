import pygame
import pygame.freetype
import os
from random import choice, randint
from itertools import cycle
pygame.init()


screen = pygame.display.set_mode((800, 500))

RESOLUTION = 800, 600
FPS = 60
TILESIZE = 32
PLAYER_SPEED = 300
FALLING_SPEED = 200
ANIM_THRESHOLD = 0.05

black = (0, 0, 0)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((800/2),(500/2))
    screen.blit(TextSurf, TextRect)

playerimg = pygame.image.load("box.png")
playerimg = pygame.transform.scale(playerimg, (200, 100))

carimg = pygame.image.load("car.png")
carimg = pygame.transform.scale(carimg, (207, 74))

carimg2 = pygame.image.load("car.png")
carimg2 = pygame.transform.scale(carimg, (207, 74))

carimg3 = pygame.image.load("car.png")
carimg3 = pygame.transform.scale(carimg, (207, 74))

carimg4 = pygame.image.load("car.png")
carimg4 = pygame.transform.scale(carimg, (207, 74))

b_carimg = pygame.image.load("burning_car.png")
b_carimg = pygame.transform.scale(b_carimg, (207, 147))

b_carimg2 = pygame.image.load("burning_car.png")
b_carimg2 = pygame.transform.scale(b_carimg2, (207, 147))

broken = False
hit = 0
howmany = 0

bg = pygame.image.load("background.png")

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, falling_stuff, *grps):
        super().__init__(*grps)

        self.images = []

        img = pygame.image.load(os.path.join('box.png')).convert()
        self.images.append(img)
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

        self.hitbox.center = self.rect.center
        self.hitbox.move_ip(5 if self.direction == 'LEFT' else 10, 10)

        pygame.display.update()
        
    

class FallingStuff(pygame.sprite.Sprite):
    def __init__(self, pos, *grps):
        super().__init__(*grps)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(choice(['blue', 'yellow', 'green']))
        self.rect = self.image.get_rect(topleft=pos)

        
    def update(self, dt, events):
        self.rect.move_ip(0, FALLING_SPEED * dt)
        display_rect = pygame.display.get_surface().get_rect()
        broken == False
        hit = 0
        if self.rect.top > 420:
            self.kill()
            hit = hit + 1
            broken == True
            print ("meow")
            self.burning = True

            pygame.display.update()
        

           
             

   

class Car1(pygame.sprite.Sprite):
    def __init__(self, game, pos, falling_stuff, *grps):
        super().__init__(*grps)
        self.groups = game.all_sprites
        self.game = game

        self.images = [carimg, b_carimg]
        
        self.burning = False

        self.burning = [b_carimg, b_carimg2]

    def update(self):  
        if broken == True:
            self.burning = True
            print ("woof")

    def animate(self):
        now = pygame.time.get_ticks()

        if self.burning:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.burning)
                self.image = self.burning[self.current_frame]


    def update(self):  
        if broken == True:
            self.burning = True
            print ("woof")

    def animate(self):
        now = pygame.time.get_ticks()

        if self.burning:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.burning)
                self.image = self.burning[self.current_frame]
           



    



