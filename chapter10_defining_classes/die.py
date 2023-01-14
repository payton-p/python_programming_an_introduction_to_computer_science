from chapter0_provided_graphics.graphics import Circle, Point, Rectangle


class Die:
    """Die displays a graphical representation of a standard six-sided die."""

    def __init__(self, window, center, size):
        """Create a view of a die."""

        self.window = window  # save this for drawing pips later
        self.background = "white"  # color of die face
        self.foreground = "black"  # color of the pips
        self.pip_radius = 0.1 * size  # radius of each pip
        half_die_size = size / 2.0  # half the size of the die
        offset = 0.6 * half_die_size  # distance from center to outer pips

        # Create a square for the face.
        center_x, center_y = center.get_x(), center.get_y()
        point1 = Point(center_x - half_die_size, center_y - half_die_size)
        point2 = Point(center_x + half_die_size, center_y + half_die_size)
        rectangle = Rectangle(point1, point2)
        rectangle.draw(window)
        rectangle.set_fill(self.background)

        # Create 7 circles for standard pip locations.
        self.pip1 = self.__make_pip(center_x - offset, center_y - offset)
        self.pip2 = self.__make_pip(center_x - offset, center_y)
        self.pip3 = self.__make_pip(center_x - offset, center_y + offset)
        self.pip4 = self.__make_pip(center_x, center_y)
        self.pip5 = self.__make_pip(center_x + offset, center_y - offset)
        self.pip6 = self.__make_pip(center_x + offset, center_y)
        self.pip7 = self.__make_pip(center_x + offset, center_y + offset)

        # Draw an initial value. 
        self.set_value(1)

    def __make_pip(self, x, y):
        """Draw a pip at (x,y)."""

        pip = Circle(Point(x, y), self.pip_radius)
        pip.set_fill(self.background)
        pip.set_outline(self.background)
        pip.draw(self.window)

        return pip

    def set_value(self, value):
        """Set display of die based on the value."""

        # Hide all pips.
        self.pip1.set_fill(self.background)
        self.pip2.set_fill(self.background)
        self.pip3.set_fill(self.background)
        self.pip4.set_fill(self.background)
        self.pip5.set_fill(self.background)
        self.pip6.set_fill(self.background)
        self.pip7.set_fill(self.background)

        # Display correct pips.
        if value == 1:
            self.pip4.set_fill(self.foreground)
        elif value == 2:
            self.pip1.set_fill(self.foreground)
            self.pip7.set_fill(self.foreground)
        elif value == 3:
            self.pip1.set_fill(self.foreground)
            self.pip7.set_fill(self.foreground)
            self.pip4.set_fill(self.foreground)
        elif value == 4:
            self.pip1.set_fill(self.foreground)
            self.pip3.set_fill(self.foreground)
            self.pip5.set_fill(self.foreground)
            self.pip7.set_fill(self.foreground)
        elif value == 5:
            self.pip1.set_fill(self.foreground)
            self.pip3.set_fill(self.foreground)
            self.pip4.set_fill(self.foreground)
            self.pip5.set_fill(self.foreground)
            self.pip7.set_fill(self.foreground)
        else:
            self.pip1.set_fill(self.foreground)
            self.pip2.set_fill(self.foreground)
            self.pip3.set_fill(self.foreground)
            self.pip5.set_fill(self.foreground)
            self.pip6.set_fill(self.foreground)
            self.pip7.set_fill(self.foreground)
