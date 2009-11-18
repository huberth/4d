import os
import sys
sys.path += [os.path.join(sys.path[0], "src")]
import pygame

import ui
import input
import game
import objects

screens = ui.ScreenStack()
player = objects.Player(10, 0.04, [0.5, 0.5, 0.2, 0.8] )
screens.push(game.Game(player))

while 1:
    screens.main_loop()

