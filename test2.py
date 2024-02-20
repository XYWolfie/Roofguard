import random
import pygame as pg
from pygame.sprite import Sprite
vec = pg.math.Vector2

screen_width = 640
screen_height = 480
bg_color = ((100, 0, 200))


character = pg.image.load("Black-Rectangle-PNG.png") #characterleft0
character = pg.transform.scale(character, (45,60)) 

class Character(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups =  game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        pg.sprite.Sprite.__init__(self)
        self.image = character
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
                self.image = character

        if keys[pg.K_d]:
                self.pos.x += self.speed
                self.image = character

        self.rect.center = self.pos
        screen.blit(self.image, self.rect)



def run_game():
    pg.init()
    clock = pg.time.Clock()
    bg_settings = Settings()
    screen = pg.display.set_mode(
        (bg_settings.screen_width, bg_settings.screen_height))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.fill(bg_settings.bg_color)
        character.draw(screen)
            
        clock.tick(60)

run_game()