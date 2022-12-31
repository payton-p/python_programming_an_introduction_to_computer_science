from oval import Oval
from point import Point


class Circle(Oval):
    """A Circle object represents a circle graphic that can be drawn."""

    def __init__(self, center, radius):
        """Construct a circle with given center point and radius."""

        point1 = Point(center.x - radius, center.y - radius)
        point2 = Point(center.x + radius, center.y + radius)
        Oval.__init__(self, point1, point2)
        self.radius = radius

    def clone(self):
        """Return a clone of the circle."""

        other = Circle(self.get_center(), self.radius)
        other.config = self.config.copy()

        return other

    def get_radius(self):
        """Return the radius of the circle."""

        return self.radius
