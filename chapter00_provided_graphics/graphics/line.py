from _bounding_box import _BoundingBox
from _config import DEFAULT_CONFIG, BAD_OPTION_ERROR_MESSAGE
from _graphics_error import _GraphicsError


class Line(_BoundingBox):
    """A Line object represents a line graphic that can be drawn."""

    def __init__(self, point1, point2):
        """Construct a line segment from point1 to point2."""

        _BoundingBox.__init__(self, point1, point2, ["arrow", "fill", "width"])
        self.set_fill(DEFAULT_CONFIG['outline'])
        self.set_outline = self.set_fill

    def clone(self):
        """Return a clone of the object."""

        other = Line(self.point1, self.point2)
        other.config = self.config.copy()

        return other

    def set_arrow(self, option):
        """
        Set the arrowhead status of a line.

        Arrows may be drawn at either the first point, the last point, or both. Possible option values are "first",
        "last", "both", and "none".
        """

        if option not in ["first", "last", "both", "none"]:
            raise _GraphicsError(BAD_OPTION_ERROR_MESSAGE)

        self._reconfig("arrow", option)

    def _draw(self, canvas, options):
        """Draw the object in a GraphicsWindow."""

        point1 = self.point1
        point2 = self.point2
        x1, y1 = canvas.get_screen_coords(point1.x, point1.y)
        x2, y2 = canvas.get_screen_coords(point2.x, point2.y)

        return canvas.create_line(x1, y1, x2, y2, options)
