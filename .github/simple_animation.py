#Simple Animation with PyGame, Jeremiah Harrell, 12/09/2021, 9:05AM, v0.2

import pygame, sys, time 
from pygame.locals import *

# Set up PyGame
pygame.init()

# Setup the Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.displa.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animaiton Example!')

# Setup the direion variables.
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4