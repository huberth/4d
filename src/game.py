import pygame
import os

import ui
import input
import objects

game = None

class Game(ui.Screen):
    def __init__(self, player):
        ui.Screen.__init__(self)

        self.xy = [0, 1]
        self.zw = [2, 3]

        self.player      = player
        self.allies      = []
        self.enemies     = []
        self.projectiles = []

        self.info = [ FramerateDisplay(),
                      HUD(self.player, self.enemies) ]
        self.update_objects = [ self.enemies, self.allies, self.projectiles, [self.player] ]
        self.draw_objects = [ self.info ] + self.update_objects
        
        global game
        game = self

    def get_xy(self, pos):
        return (pos[self.xy[0]], pos[self.xy[1]])

    def get_color(self, pos):
        z = pos[self.zw[0]]
        w = pos[self.zw[1]]
        if z < 0: z = 0
        if z > 1: z = 1
        if w < 0: w = 0
        if w > 1: w = 1
        return pygame.Color(255, int(z * 255.0), int(w * 255.0))

    def draw(self, surface):
        for lst in self.draw_objects:
            for obj in lst:
                obj.draw(surface)

    def game_obj_count(self):
        return 1 + len(self.enemies) + len(self.projectiles) + len(self.allies)

    def update(self, inputs):
        # update objects
        for lst in self.update_objects:
            for obj in lst:
                projectiles = obj.update(inputs)
                if projectiles is not None:
                    self.projectiles += projectiles

        # collision detection
        self._do_collisions()

        # remove any object marked as deleted
        for lst in self.update_objects:
            self._remove_deleted_objects(lst)

        return True

    def _remove_deleted_objects(self, lst):
        for obj in lst:
            if obj.deleted:
                lst.remove(obj)

    def _do_collisions(self):
        # collide projectiles with allies, enemies, and players
        for proj in self.projectiles:
            p = proj.shape()

            if isinstance(proj.source, objects.Player):
                check_types = [self.enemies]
            elif isinstance(proj.source, objects.Enemy):
                check_types = [[self.player], self.allies]
            elif isinstance(proj.source, objects.NP):
                check_types = [self.enemies]

            for lst in check_types:
                # break out if the projectile's already hit something
                if proj.deleted: break

                for obj in lst:
                    if proj.deleted: break

                    # if the thing we are testing against is not dead
                    if not obj.deleted:
                        o = obj.shape()
                        if p.collides_with(o):
                            obj.collide(proj)
                            proj.collide(obj)

##################################################

class FramerateDisplay:
    def __init__(self):
        self.clock    = ui.clock
        self.interval = ui.fps
        self.font     = ui.font[20]
        self.size     = -1
        self.count    = 0

    def draw(self, surface):
        if self.count == 0:
            fps = self.clock.get_fps()
            s = "%.2f %d" % (fps, game.game_obj_count())
            self.size = self.font.size(s)
            self.surface = self.font.render(s, True, pygame.Color(192,192,192))
        surface.blit(self.surface, (10, ui.res[1] - self.size[1] - 10))

class HUD:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies
        img = pygame.image.load(os.path.join("resources", "img", "hud.png"))
        self.image = pygame.transform.scale(img, (128,128))
        
    def draw(self, surface):
        surface.blit(self.image, (10,10))
        
        pos = (10 + int(128 * self.player.pos[game.zw[0]]),
               10 + int(128 * self.player.pos[game.zw[1]]))
        pygame.draw.circle(surface, pygame.Color(127,127,127), pos, 5, 0)
        
        # TODO: draw enemies
