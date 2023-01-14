class _Transform:
    """Internal class for 2-D coordinate transformations."""

    def __init__(self, window_width, window_height, x_lower_left, y_lower_left, x_upper_right, y_upper_right):
        """Construct a new _Transform object."""

        # (x_lower_left, y_lower_left) are coordinates of lower-left, raw (0, window_height-1).
        # (x_upper_right, y_upper_right) are coordinates of upper-right, raw (window_width-1, 0).
        x_span = (x_upper_right - x_lower_left)
        y_span = (y_upper_right - y_lower_left)
        self.x_base = x_lower_left
        self.y_base = y_upper_right
        self.x_scale = x_span / float(window_width - 1)
        self.y_scale = y_span / float(window_height - 1)

    def get_screen_coords(self, x, y):
        """Return x,y in screen (actual window) coordinates."""

        xs = (x - self.x_base) / self.x_scale  # the "s" in xs is referencing the x screen coordinate, same for y
        ys = (self.y_base - y) / self.y_scale

        return int(xs + 0.5), int(ys + 0.5)

    def get_world_coords(self, xs, ys):
        """
        Return xs,ys in world coordinates.

        World Coordinates: The positions of collections of points (objects) relative to a single shared standard
        zero point. Also known as the "universe" or sometimes "model" coordinate system. This is the base reference
        system for the overall model, (generally in 3D), to which all other model coordinates relate.
        """

        x = xs * self.x_scale + self.x_base
        y = self.y_base - ys * self.y_scale

        return x, y
