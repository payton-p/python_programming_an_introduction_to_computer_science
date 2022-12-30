from _graphics_object import _GraphicsObject
from point import Point


class _BoundingBox(_GraphicsObject):
    """Internal base class for objects represented by a bounding box (Line, Oval, Rectangle)."""

    def __init__(self, point1, point2, options=None):
        """Construct a new _BoundingBox object."""

        if options is None:
            options = ["outline", "width", "fill"]

        _GraphicsObject.__init__(self, options)
        self.point1 = point1.clone()
        self.point2 = point2.clone()

    def get_point1(self):
        """Return point1 of bounding box."""

        return self.point1.clone()

    def get_point2(self):
        """Return point2 of bounding box."""

        return self.point2.clone()

    def get_center(self):
        """Return center point of bounding box."""

        p1 = self.point1
        p2 = self.point2

        return Point((p1.x + p2.x) / 2.0, (p1.y + p2.y) / 2.0)

    def _move(self, dx, dy):
        """Update internal state of object to move it dx,dy units."""

        self.point1.x = self.point1.x + dx
        self.point1.y = self.point1.y + dy
        self.point2.x = self.point2.x + dx
        self.point2.y = self.point2.y + dy
