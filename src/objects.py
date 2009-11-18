import pygame
import game


class GameObject:
    """
    Base class for every in-game object: ships for players and enemies,
    and shots (of various kinds).
    """

    def __init__(self):
        self.deleted = False

    def draw(self, surface):
        pass

    def update(self, inputs):
        pass

##################################################

class Ship(GameObject):
    """
    Base class for all ships (enemy, ally, player) that appear in the game.
    """

    def __init__(self, hp):
        """
        Creates a new ship with the given maximum HP.
        """
        GameObject.__init__(self)
        self.hp = hp
        self.max_hp = hp

##################################################

class Player(Ship):
    """
    Class for any player-controlled ship.
    """

    def __init__(self, hp, pos):
        Ship.__init__(self, hp)
        self.pos = pos
        
    def draw(self, surface):
        surface.fill( pygame.Color(128,128,128),
                      pygame.Rect(75, 75, 100, 125) )
