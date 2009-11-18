import pygame

import ui
import input

game = None

class Game(ui.Screen):
    def __init__(self, player):
        ui.Screen.__init__(self)

        self.player      = player
        self.allies      = []
        self.enemies     = []
        self.projectiles = []

        self.info = [ ]
        self.update_objects = [ self.enemies, self.allies, self.projectiles, [self.player] ]
        self.draw_objects = [ self.info ] + self.update_objects
        
        global game
        game = self

    def draw(self, surface):
        for lst in self.draw_objects:
            for obj in lst:
                obj.draw(surface)

    def update(self, inputs):
        # update objects
        for lst in self.update_objects:
            for obj in lst:
                obj.update(inputs)

        return True
