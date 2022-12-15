from _bounding_box import _BoundingBox


class Oval(_BoundingBox):
    def __init__(self, p1, p2):
        _BoundingBox.__init__(self, p1, p2)

    def clone(self):
        other = Oval(self.p1, self.p2)
        other.config = self.config.copy()

        return other

    def _draw(self, canvas, options):
        p1 = self.p1
        p2 = self.p2
        x1, y1 = canvas.to_screen(p1.x, p1.y)
        x2, y2 = canvas.to_screen(p2.x, p2.y)
        
        return canvas.create_oval(x1, y1, x2, y2, options)
