class _Transform:
    """Internal class for 2-D coordinate transformations."""

    def __init__(self, w, h, xlow, ylow, xhigh, yhigh):
        # w, h are width and height of the window
        # (xlow,ylow) are coordinates of lower-left [raw (0,h-1)]
        # (xhigh,yhigh) are coordinates of upper-right [raw (w-1,0)]
        xspan = (xhigh - xlow)
        yspan = (yhigh - ylow)
        self.xbase = xlow
        self.ybase = yhigh
        self.xscale = xspan / float(w - 1)
        self.yscale = yspan / float(h - 1)

    def get_screen_coords(self, x, y):
        """Return x,y in screen (actual window) coordinates."""

        xs = (x - self.xbase) / self.xscale
        ys = (self.ybase - y) / self.yscale

        return int(xs + 0.5), int(ys + 0.5)

    def get_world_coords(self, xs, ys):
        """
        Return xs,ys in world coordinates.

        World Coordinates: The positions of collections of points (objects) relative to a single shared standard
        zero point. Also known as the "universe" or sometimes "model" coordinate system. This is the base reference
        system for the overall model, (generally in 3D), to which all other model coordinates relate.
        """

        x = xs * self.xscale + self.xbase
        y = self.ybase - ys * self.yscale

        return x, y
