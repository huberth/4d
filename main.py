import sys
import os
sys.path += [os.path.join(sys.path[0], "src")]

import ui
import pygame

clock = pygame.time.Clock()

while True:
    ui.draw(clock)
    clock.tick(60)
