import math

class Shape:
    """
    Base class for a bounding shape used for collision detection.
    """

    def collide(self, obj):
        if obj is None: return False

        if isinstance(obj, Sphere):
            return self.collide_sphere(obj)
        elif isinstance(obj, Cube):
            return self.collide_cube(obj)
        else:
            raise Exception("not sure what shape you have here: " + obj)

    def collide_sphere(self, obj):
        return False

    def collide_cube(self, obj):
        return False

class Sphere(Shape):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def collide_sphere(self, sphere):
        distance = math.sqrt(sum(map(lambda x,y: math.pow(x-y,2.0),
                                     self.center, sphere.center)))
        return distance <= (self.radius + sphere.radius)

class Cube(Shape):
    def __init__(self, center, side):
        self.center = center
        self.side = side
