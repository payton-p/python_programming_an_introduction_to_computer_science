from graphics_object import GraphicsObject
from point import Point
from graphics_window import GraphicsWindow


class Polygon(GraphicsObject):
    def __init__(self, *points):
        # if points passed as a list, extract it

        if len(points) == 1 and isinstance(points[0], type([])):
            points = points[0]
        self.points = list(map(Point.clone, points))
        GraphicsObject.__init__(self, ["outline", "width", "fill"])

    def clone(self):
        other = Polygon(*self.points)
        other.config = self.config.copy()
        return other

    def get_points(self):
        return list(map(Point.clone, self.points))

    def _move(self, dx, dy):
        for p in self.points:
            p.move(dx, dy)

    def _draw(self, canvas, options):
        args = [canvas]
        for p in self.points:
            x, y = canvas.to_screen(p.x, p.y)
            args.append(x)
            args.append(y)
        args.append(options)
        return GraphicsWindow.create_polygon(*args)
