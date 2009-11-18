class Movement:
    """
    Class describing how a game object moves in 4-space.
    """

    def __init__(self, owner):
        self.pos = [0,0,0,0]
        self.owner = owner

    def update(self):
        pass

class Firing:
    """
    Class describing how an NP ship fires projectiles over time.
    """

    def __init__(self, owner):
        self.owner = owner

    def update(self):
        """
        Updates internal state, and returns a (possibly empty)
        list of projectiles fired during the current frame.
        """
        return []

##################################################

class LinearMovement(Movement):
    def __init__(self, owner, vel):
        Movement.__init__(self, owner)
        self.pos = owner.pos[:]
        self.vel = vel

    def update(self):
        for i in range(4):
            self.pos[i] += self.vel[i]
