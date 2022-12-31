from _bounding_box import _BoundingBox


class Rectangle(_BoundingBox):
    """A Rectangle object represents a rectangle graphic that can be drawn."""

    def __init__(self, point1, point2):
        """Construct a rectangle that has opposite corners at point1 and point2."""

        _BoundingBox.__init__(self, point1, point2)

    def clone(self):
        """Return a clone of the object."""

        other = Rectangle(self.point1, self.point2)
        other.config = self.config.copy()

        return other

    def _draw(self, canvas, options):
        """Draw the object in a GraphicsWindow."""

        point1 = self.point1
        point2 = self.point2
        x1, y1 = canvas.get_screen_coords(point1.x, point1.y)
        x2, y2 = canvas.get_screen_coords(point2.x, point2.y)

        return canvas.create_rectangle(x1, y1, x2, y2, options)
