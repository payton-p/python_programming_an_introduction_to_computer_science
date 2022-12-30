from _bounding_box import _BoundingBox


class Rectangle(_BoundingBox):
    def __init__(self, point1, point2):
        _BoundingBox.__init__(self, point1, point2)

    def _draw(self, canvas, options):
        p1 = self.point1
        p2 = self.point2
        x1, y1 = canvas.get_screen_coords(p1.x, p1.y)
        x2, y2 = canvas.get_screen_coords(p2.x, p2.y)

        return canvas.create_rectangle(x1, y1, x2, y2, options)

    def clone(self):
        other = Rectangle(self.point1, self.point2)
        other.config = self.config.copy()

        return other
