import os
import sys
sys.path += [os.path.join(sys.path[0], "src")]
import pygame

import ui
import input
import game
import objects

screens = ui.ScreenStack()
player = objects.Player(10, None)
screens.push(game.Game(player))

while 1:
    screens.main_loop()
#while not game.game_over:
