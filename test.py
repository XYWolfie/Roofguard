import pygame
import pygame.freetype
import os
from random import choice, randint
from itertools import cycle
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Roofguard")

RESOLUTION = 800, 600
FPS = 10
TILESIZE = 32
PLAYER_SPEED = 400
FALLING_SPEED = 200
ANIM_THRESHOLD = 0.05

window = 0

game_start = True
game_playing = False
game_over = False

black = (0, 0, 0)
red = (73, 12, 15)
white = (255, 255, 255)

txt = pygame.freetype.Font("prstart.ttf", 34)
game_over_text = txt.render("Game over, click R to restart", False, ('red'))

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

score = 0

bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (800, 600))

screen = pygame.display.set_mode((800, 600))

def draw_start_menu():
    logo = pygame.image.load("pixel_logo.png")
    logo = pygame.transform.scale(logo, (720, 100))
    screen.fill((white))
    font = pygame.freetype.Font("prstart.ttf", 24)
    font.render_to(screen, (160, 450), f"press 'space' to start", 'black')
    screen.blit(logo, (800/2 - logo.get_width()/2, 200))

def draw_game_over():
    screen.fill((black))
    font = pygame.freetype.Font("prstart.ttf", 24)
    font2 = pygame.freetype.Font("prstart.ttf", 64)
    font.render_to(screen, (100, 250), f'GAME OVER', 'red')
    font.render_to(screen, (160, 450), f"Press 'r to restart", 'white')
    txt.render_to(screen, (20, 20), f' Your score: {score}', 'white')

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, falling_stuff, *grps):
        super().__init__(*grps)
        self.images = [pygame.image.load(os.path.join('roofguard.png')).convert()]
        self.image = self.images[0]
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.update()
        self.image = playerimg
        self.direction = "LEFT"
        self.animation_counter = 0
        self.rect = self.image.get_rect(topleft=pos)
        self.falling_stuff = falling_stuff
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
        global score

        self.rect.move_ip(d * dt * PLAYER_SPEED, 0)
        display_rect = pygame.display.get_surface().get_rect()
        self.rect.clamp_ip(display_rect)

        for stuff in self.falling_stuff:
            if self.hitbox.colliderect(stuff.rect):
                stuff.kill()
                score += 1

                if score >= 0:
                    PLAYER_SPEED = 450
                    FALLING_SPEED = 200
                if score >= 5:
                    PLAYER_SPEED = 500
                    FALLING_SPEED = 250
                # ... add more score-based speed adjustments

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
        global game_playing
        global game_over
        global display_rect
        self.rect.move_ip(0, FALLING_SPEED * dt)
        display_rect = pygame.display.get_surface().get_rect()
        global window

        if self.rect.top > 500:
            if 200 < self.rect.left < 600:
                self.kill()
                x_pos = -150 if self.rect.left < 200 else 580
                screen.blit(b_carimg, (x_pos, 340))

                font = pygame.font.Font("prstart.ttf", 64)
                font.render_to(screen, (100, 250), f'GAME OVER', 'red')

                game_playing = False
                game_over = True
                window = 2

def playing(player, falling_stuff, dt, clock):
    global game_playing
    global window
    global game_over
    if game_playing:
        sprites = pygame.sprite.Group()
        sprites.add(player)
        sprites.add(falling_stuff)

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
            txt.render_to(screen, (20, 20), f'Score: {score}', 'black')
            sprites.draw(screen)
            screen.blit(carimg, (-150, 465))
            screen.blit(carimg2, (215, 465))
            screen.blit(carimg3, (580, 465))
            sprites.update(dt, events)
            pygame.display.flip()
            dt = clock.tick(FPS) / 1000

def start():
    global game_start
    global window
    global game_playing
    global player_y
    global player_x
    screen.fill((0, 0, 0))  
    draw_start_menu()
    if game_start:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player_x = 200
            player_y = 400
            game_start = False
            game_playing = True
            window = 1

       
def gameover():
    global game_over
    global window
    global game_start
    if game_over:
        screen.fill((0, 0, 0))  # Fill the screen with black
        draw_game_over()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_over = False
            game_start = True
            window = 0

def main():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if window == 0:
            start()

        elif window == 1:
            playing()

        elif window == 2:
            gameover()

        pygame.display.update()
        clock.tick(FPS)
main()