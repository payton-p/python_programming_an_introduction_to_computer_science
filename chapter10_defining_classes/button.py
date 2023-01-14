from chapter00_provided_graphics.graphics import Point, Rectangle, Text


class Button:
    """A button is a labeled rectangle in a window that performs actions."""

    def __init__(self, window, center, width, height, label):
        """Create a rectangular button."""

        w, h = width / 2.0, height / 2.0
        x, y = center.get_x(), center.get_y()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        point1 = Point(self.xmin, self.ymin)
        point2 = Point(self.xmax, self.ymax)
        self.rectangle = Rectangle(point1, point2)
        self.rectangle.set_fill("lightgray")
        self.rectangle.draw(window)
        self.label = Text(center, label)
        self.label.draw(window)
        self.active = False

    def clicked(self, point):
        """Return true if button is clicked."""

        return self.active and self.xmin <= point.get_x() <= self.xmax and self.ymin <= point.get_y() <= self.ymax

    def get_label(self):
        """Return the label for this button."""

        return self.label.get_text()

    def set_active_status(self, is_active):
        """Set button's active status."""

        if is_active:
            self.label.set_fill('black')
            self.rectangle.set_width(2)
            self.active = True
        else:
            self.label.set_fill('darkgrey')
            self.rectangle.set_width(1)
            self.active = False
