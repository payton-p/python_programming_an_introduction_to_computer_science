from _bounding_box import _BoundingBox
from _graphics_error import _GraphicsError
from _config import DEFAULT_CONFIG, BAD_OPTION_ERROR_MESSAGE


class Line(_BoundingBox):
    def __init__(self, p1, p2):
        _BoundingBox.__init__(self, p1, p2, ["arrow", "fill", "width"])
        self.set_fill(DEFAULT_CONFIG['outline'])
        self.set_outline = self.set_fill

    def clone(self):
        other = Line(self.p1, self.p2)
        other.config = self.config.copy()

        return other

    def _draw(self, canvas, options):
        p1 = self.p1
        p2 = self.p2
        x1, y1 = canvas.to_screen(p1.x, p1.y)
        x2, y2 = canvas.to_screen(p2.x, p2.y)

        return canvas.create_line(x1, y1, x2, y2, options)

    def set_arrow(self, option):
        if option not in ["first", "last", "both", "none"]:
            raise _GraphicsError(BAD_OPTION_ERROR_MESSAGE)

        self._reconfig("arrow", option)
