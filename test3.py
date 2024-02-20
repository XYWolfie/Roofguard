import random
import pygame as pg
from pygame.sprite import Sprite
vec = pg.math.Vector2

vel = 1
amount = 0

class Settings:
    screen_width = 640
    screen_height = 480
    bg_color = ((100, 0, 200))

roofguard = pg.image.load("Black-Rectangle-PNG.png")
roofguard = pg.transform.scale(roofguard, (200, 100))



class Roofguard(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups =  game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        pg.sprite.Sprite.__init__(self)
        self.image = roofguard
        self.rect = self.image.get_rect()
        self.pos = vec(270, 60)
        self.speed = 2
        self.score = 0
        self.rect.center = self.pos
        self.image = pg.surface((100, 100))

    def update(self):
        self.rect.center = self.pos

        if self.pos.x > 640:
            self.pos.x = 640

        if self.pos.x < 0:
            self.pos.x = 0

        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            
                self.pos.x -= self.speed
                self.image = roofguard

        if keys[pg.K_d]:
                self.pos.x += self.speed
                self.image = roofguard

        self.rect.center = self.pos

class Ball(Sprite):
    """A class to represent a single ball."""



    def __init__(self, bg_settings, screen):
        """Initalize the ball and set its starting position."""
        super(Ball, self).__init__()
        self.screen = screen
        self.bg_settings = bg_settings
        self.image = pg.Surface((30, 30))
        self.image.fill((100, 200, 0))
        self.rect = self.image.get_rect()
        # Start each new ball.
        self.rect.x = random.randint(-10, self.bg_settings.screen_width)
        self.rect.y = random.randint(-100, -40)
        # Store the ball's exact position.
        self.y = float(self.rect.y)

    def update(self):
        """Move the ball down."""
        self.y += 1
        self.rect.y = self.y

        if self.rect.top > self.bg_settings.screen_height:
            self.kill()



def run_game():
    pg.init()
    clock = pg.time.Clock()
    bg_settings = Settings()
    screen = pg.display.set_mode(
        (bg_settings.screen_width, bg_settings.screen_height))
    balls = pg.sprite.Group()
    roofguards = pg.sprite.Group()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        roofguards.update()
        if roofguard == amount:
            roofguards.add(Roofguard(bg_settings, screen))

        balls.update()
        if random.randrange(200) < 1:
            balls.add(Ball(bg_settings, screen))

        screen.fill(bg_settings.bg_color)
        balls.draw(screen)
        roofguards.draw(screen)

        pg.display.flip()
        clock.tick(60)


run_game()



if broken == True:
            print ("woof")
            self.image = self.images[1]
            self.rect = self.image.get_rect(topleft=pos)
        else:
            self.image = self.images[0]
            self.rect = self.image.get_rect(topleft=pos)



  def update(self, dt, events):
        self.rect.move_ip(0, FALLING_SPEED * dt)
        display_rect = pygame.display.get_surface().get_rect()
        broken == False
        hit = 0
        if self.rect.top > 420:
            self.kill()
            hit = hit + 1
            message_display('Game over')


        if hit >= 1:
            broken == True
            print("meow")
            print(hit)




def main():

    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION)

    

    dt, clock = 0, pygame.time.Clock()
    sprites = pygame.sprite.Group()
    falling_stuff = pygame.sprite.Group()
    player = Player((300, 300), falling_stuff, sprites)
    
    font = pygame.freetype.SysFont('Arial', 54)

    CREATE_STUFF = pygame.USEREVENT + 1
    pygame.time.set_timer(CREATE_STUFF, randint(1000, 2000), True)
    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
            if e.type == CREATE_STUFF:
                pygame.time.set_timer(CREATE_STUFF, randint(1000, 2000), True)
                FallingStuff((randint(50, 550), -TILESIZE), falling_stuff, sprites)
        
        screen.fill('white')
        font.render_to(screen, (20, 20), f'Score: {player.score}', 'black')
        sprites.draw(screen)
        screen.blit(carimg, (5,420))
        screen.blit(carimg2, (230,420))
        screen.blit(carimg3, (455,420))
        screen.blit(carimg4, (680,420))
        sprites.update(dt, events)
        pygame.display.flip()
        dt = clock.tick(FPS) / 1000

        pygame.display.update()
        


if __name__ == "__main__":
    main()


    def main():

    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION)

    

    dt, clock = 0, pygame.time.Clock()
    sprites = pygame.sprite.Group()
    falling_stuff = pygame.sprite.Group()
    player = Player((300, 300), falling_stuff, sprites)
    
    font = pygame.freetype.SysFont('Arial', 54)

    CREATE_STUFF = pygame.USEREVENT + 1
    pygame.time.set_timer(CREATE_STUFF, randint(1000, 2000), True)
    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
            if e.type == CREATE_STUFF:
                pygame.time.set_timer(CREATE_STUFF, randint(1000, 2000), True)
                FallingStuff((randint(50, 550), -TILESIZE), falling_stuff, sprites)
        
        screen.fill('white')
        font.render_to(screen, (20, 20), f'Score: {player.score}', 'black')
        sprites.draw(screen)
        screen.blit(carimg, (5,420))
        screen.blit(carimg2, (230,420))
        screen.blit(carimg3, (455,420))
        screen.blit(carimg4, (680,420))
        sprites.update(dt, events)
        pygame.display.flip()
        dt = clock.tick(FPS) / 1000

        pygame.display.update()
        


if __name__ == "__main__":
    main()


-------------------------------------------


import pygame
import pygame.freetype
import os
from random import choice, randint
from itertools import cycle
from sprites import *
pygame.init()







class Game():
    def __init__(self):
          
        self.RESOLUTION = 800, 600
        self.FPS = 60
        self.TILESIZE = 32
        self.PLAYER_SPEED = 400
        self.FALLING_SPEED = 200
        self.ANIM_THRESHOLD = 0.05

        self.black = (0, 0, 0)
        self.red = (73, 12, 15)

        self.comic_sans50 = pygame.font.SysFont("Comic Sans MS", 50) 

        self.broken = False
        self.hit = 0
        self.howmany = 0
        
        self.screen = pygame.display.set_mode((800, 600))
        self.bg = pygame.image.load("bg.png")
        self.bg = pygame.transform.scale(self.bg, (800, 600))

    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def message_display(text):
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((800/2),(500/2))
        screen.blit(TextSurf, TextRect)

   

            



    
    def end(self, event):
        
        while self.game_over:
            self.clock.tick(self.FPS)
            self.game_over_text = self.comic_sans50.render("Game over, click R to restart", False, (self.red))
            self.back_to_menu_text = self.comic_sans50.render("Click B to reach the menu", False, (self.red))
            self.score_text = self.comic_sans50.render("SCORE:" + str(self.player.score), False, (self.red))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = False
                    pygame.quit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        self.game_over = False
                    if event.key == pygame.K_r:  # om vi clicker på R, avslutter vi game over loop, og går derett til self.new() som ligger etter game_over loop
                        self.game_over = False 


    def main(self):

        pygame.init()
        self.screen = pygame.display.set_mode(RESOLUTION)

        

        self.dt, self.clock = 0, pygame.time.Clock()
        self.sprites = pygame.sprite.Group()
        self.falling_stuff = pygame.sprite.Group()
        self.player = Player((300, 360), self.falling_stuff, self.sprites)
        
        self.font = pygame.freetype.SysFont('comic sans', 40)

        CREATE_STUFF = pygame.USEREVENT + 1
        pygame.time.set_timer(CREATE_STUFF, randint(1000, 2000), True)
        while True:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    return
                if e.type == CREATE_STUFF:
                    pygame.time.set_timer(CREATE_STUFF, randint(1000, 2000), True)
                    FallingStuff((randint(50, 550), -TILESIZE), self.falling_stuff, self.sprites)
            
            self.screen.fill(black)
            self.screen.blit(self.bg, (0, 0))
            self.font.render_to(screen, (20, 20), f'Score: {self.player.score}', 'black')
            self.sprites.draw(screen)
            self.screen.blit(carimg, (-150,465))
            self.screen.blit(carimg2, (215,465))
            self.screen.blit(carimg3, (580,465))
            self.sprites.update(self.dt, events)
            pygame.display.flip()
            self.dt = self.clock.tick(FPS) / 1000

            pygame.display.update()
            
            


    if __name__ == "__main__":
        main()