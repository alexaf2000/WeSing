import pygame
from viewmodel.sing_screen import set_video

FPS = 60


# screen = pygame.display.set_mode((400, 400))
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
set_video()

pygame.quit()