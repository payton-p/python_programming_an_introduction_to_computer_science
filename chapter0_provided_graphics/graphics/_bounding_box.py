from graphics_object import GraphicsObject
from point import Point


class _BoundingBox(GraphicsObject):
    """Internal base class for objects represented by a bounding
    box (Line, Oval, Rectangle).
    """

    def __init__(self, p1, p2, options=None):
        if options is None:
            options = ["outline", "width", "fill"]

        GraphicsObject.__init__(self, options)
        self.p1 = p1.clone()
        self.p2 = p2.clone()

    def _move(self, dx, dy):
        self.p1.x = self.p1.x + dx
        self.p1.y = self.p1.y + dy
        self.p2.x = self.p2.x + dx
        self.p2.y = self.p2.y + dy

    def get_p1(self):
        return self.p1.clone()

    def get_p2(self):
        return self.p2.clone()

    def get_center(self):
        p1 = self.p1
        p2 = self.p2

        return Point((p1.x + p2.x) / 2.0, (p1.y + p2.y) / 2.0)
