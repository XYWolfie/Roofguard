import pygame
import pygame.freetype
import os
from random import choice, randint
from itertools import cycle
from pygame import mixer
pygame.init()

screen = pygame.display.set_mode((800, 600))

window = 0

game_start = True
game_playing = False
game_over = False

def start():
    global game_start  
    while game_start == True:
        print ("0")
        global window
        global game_playing
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            window = 1
            game_start = False
            game_playing = True
    
def playing():
    while game_playing == True:
        print ("1")    
        global window
        global game_over
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            window = 0
            game_playing = False
            game_over = True

def gameover():
    while game_over == True:
        print ("2")
        global window
        global game_start
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            window = 0
            game_over = False
            game_start = True

def main():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    while True:
        if window == 0:
            start()
        
        elif window == 1:
            playing()

        elif window == 2:
            gameover()

main()

