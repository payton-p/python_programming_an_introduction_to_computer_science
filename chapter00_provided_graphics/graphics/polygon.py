from _graphics_object import _GraphicsObject
from graphics_window import GraphicsWindow
from point import Point


class Polygon(_GraphicsObject):
    """A Polygon object represents a polygon graphic that can be drawn."""

    def __init__(self, *points):
        """
        Construct a polygon with the given points as vertices.

        The constructor also accepts a single parameter that is a list of the vertices.
        """

        # If points were passed as a list, extract them
        if len(points) == 1 and isinstance(points[0], type([])):
            points = points[0]
        self.points = list(map(Point.clone, points))
        _GraphicsObject.__init__(self, ["outline", "width", "fill"])

    def clone(self):
        """Return a clone of the object."""

        other = Polygon(*self.points)
        other.config = self.config.copy()

        return other

    def get_points(self):
        """Return a list containing clones of the points used to construct the polygon."""

        return list(map(Point.clone, self.points))

    def _draw(self, canvas, options):
        """Draw the object in a GraphicsWindow."""

        args = [canvas]
        for point in self.points:
            x, y = canvas.get_screen_coords(point.x, point.y)
            args.append(x)
            args.append(y)
            
        args.append(options)

        return GraphicsWindow.create_polygon(*args)

    def _move(self, dx, dy):
        """Update internal state of object to move it dx,dy units."""

        for point in self.points:
            point.move(dx, dy)
