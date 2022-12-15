from graphics_object import GraphicsObject


class Point(GraphicsObject):
    def __init__(self, x, y):
        GraphicsObject.__init__(self, ["outline", "fill"])
        self.set_fill = self.set_outline
        self.x = x
        self.y = y

    def _draw(self, canvas, options):
        x, y = canvas.to_screen(self.x, self.y)
        return canvas.create_rectangle(x, y, x + 1, y + 1, options)

    def _move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def clone(self):
        other = Point(self.x, self.y)
        other.config = self.config.copy()
        return other

    def get_x(self): return self.x

    def get_y(self): return self.y
