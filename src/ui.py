import os
import sys
import pygame

pygame.init()

import input

##################################################

# global UI variables

res = ( 600, 600 )
fps = 60
clock = pygame.time.Clock()

##################################################

class FontDict:
    def __init__(self, filename):
        self.filename = os.path.join(sys.path[0], "resources", "fonts", filename)
        self.dict = {}

    def __getitem__(self, size):
        if size not in self.dict.keys():
            self.dict[size] = pygame.font.Font(self.filename, size)
        return self.dict[size]

font = FontDict("white_rabbit.ttf")

##################################################

class Screen:
    """
    Base class for anything that uses the whole screen and handles
    input events.  Basically, the game engine (game.Game)
    and menus (ui.Menu).
    """
    
    def __init__(self):
        pass

    def draw(self, surface):
        """
        Draw this screen to the given surface.
        """
        pass

    def update(self, inputs):
        """
        Update the status of this screen when given the following inputs
        for this frame.  Only the top-level screen will receive the inputs.
        
        If this method returns False, then the screen will be removed and
        the next-to-top screen will resume activity.
        """
        return True

class ScreenStack:
    """
    Handles the storage of screens.  Also initializes pygame stuff.
    """

    def __init__(self):
        pygame.display.init()
        self.stack = []
        self.surface = pygame.display.set_mode( res, pygame.DOUBLEBUF )

    def push(self, screen):
        # top of the stack is the end of the array
        self.stack.append(screen)

    def main_loop(self):
        input.read_input()

        # draw each layer, bottom to top
        self.surface.fill(pygame.Color(0,0,0))
        for screen in self.stack:
            screen.draw(self.surface)
        
        # however, only update the top surface with input
        result = self.stack[-1].update(input.last_frame)
        if not result:
            self.stack.pop()

        clock.tick(fps)

        pygame.display.flip()

##################################################

def draw(clock):
    screen.fill( pygame.Color(0,0,0) )

    screen.blit( font[16].render("%.2f" % clock.get_fps(), True,
                                 pygame.Color(255,255,255)),
                 (5, 582) )

    pygame.display.flip()
