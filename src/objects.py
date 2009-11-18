import pygame

import game
import ui
import input
import physics
import pattern

class GameObject:
    """
    Base class for every in-game object: ships for players and enemies,
    and shots (of various kinds).
    """

    def __init__(self):
        self.deleted = False
        self.pos = None

    def draw(self, surface):
        pass

    def update(self, inputs):
        pass

    def shape(self):
        """
        Returns the shape used for collision detection.
        """
        return None

##################################################

class Ship(GameObject):
    """
    Base class for all ships (enemy, ally, player) that appear in the game.
    For simplicity, all ships are hypercubic in shape, with a given side length.
    """

    def __init__(self, hp, size):
        """
        Creates a new ship with the given maximum HP.
        """
        GameObject.__init__(self)
        self.hp = hp
        self.max_hp = hp
        self.size = size

class Projectile(GameObject):
    """
    Base class for any projectile fired by a ship.
    """

    def __init__(self, source, movement):
        """
        Creates a new projectile fired by the given ship.
        """
        GameObject.__init__(self)
        self.source = source
        self.movement = movement
        self.pos = self.source.pos[:]

    def update(self, inputs):
        self.movement.update()
        self.pos = self.movement.pos

        for i in range(4):
            if self.pos[i] < -0.1 or self.pos[i] > 1.1:
                self.deleted = True

##################################################

class NP(Ship):
    """
    Class for any non-player-controlled ship.
    """
    def __init__(self, hp, size):
        Ship.__init__(self, hp, size)

class Enemy(NP):
    """
    Class for any enemy ship.
    """
    def __init__(self, hp, size):
        NP.__init__(self, hp, size)

##################################################

class Player(Ship):
    """
    Class for any player-controlled ship.
    """

    def __init__(self, hp, size, pos):
        Ship.__init__(self, hp, size)
        self.pos = pos
        
    def draw(self, surface):
        xy     = game.game.get_xy(self.pos)
        color  = game.game.get_color(self.pos)
        coords = (int(xy[0] * ui.res[0]), int(xy[1] * ui.res[1]))
        size   = int(self.size * ui.res[0])

        surface.fill( color,
                      pygame.Rect( coords[0] - size / 2, coords[1] - size / 2,
                                   size, size ) )
        pygame.draw.rect( surface,
                          pygame.Color(255,255,255),
                          pygame.Rect(coords[0] - size / 2, coords[1] - size / 2,
                                      size, size),
                          2 )

    def update(self, inputs):
        self.pos[game.game.xy[0]] += inputs[input.X_AXIS]
        self.pos[game.game.xy[1]] += inputs[input.Y_AXIS]
        self.pos[game.game.zw[0]] += inputs[input.Z_AXIS]
        self.pos[game.game.zw[1]] += inputs[input.W_AXIS]

        for i in range(4):
            if self.pos[i] < 0: self.pos[i] = 0
            if self.pos[i] > 1: self.pos[i] = 1

        if inputs[input.PRIMARY_FIRE] == 1:
            vel = [0,0,0,0]
            vel[game.game.xy[1]] = -0.01
            return [Shot(self, vel)]

    def shape(self):
        return physics.Sphere(self.pos, self.size / 2)

##################################################

class Shot(Projectile):
    """
    A basic projectile which moves in a straight line.
    """

    radius = 0.007

    def __init__(self, source, vel):
        movement = pattern.LinearMovement(source, vel)
        Projectile.__init__(self, source, movement)

    def draw(self, surface):
        xy     = game.game.get_xy(self.pos)
        color  = game.game.get_color(self.pos)
        coords = (int(xy[0] * ui.res[0]), int(xy[1] * ui.res[1]))
        size   = int(Shot.radius * ui.res[0])
        
        pygame.draw.circle( surface,
                            color,
                            (coords[0], coords[1]),
                            size,
                            0 )
