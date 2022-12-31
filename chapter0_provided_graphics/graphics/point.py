from _graphics_object import _GraphicsObject


class Point(_GraphicsObject):
    """A Point object represents a point graphic that can be drawn."""

    def __init__(self, x, y):
        """Construct a point at the given coordinates."""

        _GraphicsObject.__init__(self, ["outline", "fill"])
        self.set_fill = self.set_outline
        self.x = x
        self.y = y

    def clone(self):
        """Return a clone of the object."""

        other = Point(self.x, self.y)
        other.config = self.config.copy()

        return other

    def get_x(self):
        """Return x of the point."""

        return self.x

    def get_y(self):
        """Return y of the point."""

        return self.y

    def _draw(self, canvas, options):
        """Draw the object in a GraphicsWindow."""

        x, y = canvas.get_screen_coords(self.x, self.y)

        return canvas.create_rectangle(x, y, x + 1, y + 1, options)

    def _move(self, dx, dy):
        """Update internal state of object to move it dx,dy units."""

        self.x = self.x + dx
        self.y = self.y + dy
