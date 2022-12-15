from oval import Oval
from point import Point


class Circle(Oval):
    def __init__(self, center, radius):
        p1 = Point(center.x - radius, center.y - radius)
        p2 = Point(center.x + radius, center.y + radius)
        Oval.__init__(self, p1, p2)
        self.radius = radius

    def clone(self):
        other = Circle(self.get_center(), self.radius)
        other.config = self.config.copy()
        
        return other

    def get_radius(self):
        return self.radius
