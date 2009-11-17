import os
import sys
import pygame

pygame.init()

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

res = (600, 600)
pygame.display.init()
screen = pygame.display.set_mode( res, pygame.DOUBLEBUF )

def draw(clock):
    screen.fill( pygame.Color(0,0,0) )

    pygame.draw.rect( screen,
                      pygame.Color(100,100,100),
                      pygame.Rect(50,50,50,50),
                      1)

    screen.blit( font[16].render("%.2f" % clock.get_fps(), True,
                                 pygame.Color(255,255,255)),
                 (500, 500) )

    pygame.display.flip()
