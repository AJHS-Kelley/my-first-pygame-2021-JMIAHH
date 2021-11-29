#PyGame Practice, Jeremiah Harrell, 11/29/2021, 9:20am, v0.6

import pygame, sys
from pygame.locals import *

#start Pygame
pygame.init()

# Create game window
windowSurface = pygame.display.set_mode((500,400), 0, 32)
pygame.display.set_capiton("Hello, world!")

#Set Color Values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Setup Fonts
basicFont = pygame.font.SysFont(None, 48)

#Setup Text
text = basicFont.render('Hello, world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centery = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

#Draw background onto window surface.
windowSurface.fill(WHITE)

#Draw a green polygon onto the surface 
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
