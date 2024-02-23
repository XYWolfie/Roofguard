import pygame
import pygame.freetype
import os
from random import choice, randint
from itertools import cycle
from pygame import mixer
pygame.init()

screen = pygame.display.set_mode((800, 600))

window = 0

def start():
    global window
    while window == 0:
        pygame.event.pump()
        print ("0")
        font = pygame.freetype.Font("prstart.ttf", 64)
        font.render_to(screen, (100, 250), f'GAME START', 'red')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            window = 1
            break
    
def playing():
    global window
    while window == 1:
        pygame.event.pump()
        print ("1")    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            window = 2
            break


def gameover():
    global window
    while window == 2:
        pygame.event.pump()
        print ("2")
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            window = 0
            break

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

        pygame.display.flip()

main()

