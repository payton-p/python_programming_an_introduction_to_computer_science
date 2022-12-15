from graphics_error import GraphicsError
from config import DEFAULT_CONFIG, OBJ_ALREADY_DRAWN, UNSUPPORTED_METHOD, _root


class GraphicsObject:
    """Generic base class for all drawable objects"""

    # A subclass of GraphicsObject should override _draw and _move methods.

    def __init__(self, options):
        # options is a list of strings indicating which options are
        # legal for this object.

        # When an object is drawn, canvas is set to the GraphWin(canvas)
        #    object where it is drawn and id is the TK identifier of the
        #    drawn shape.
        self.canvas = None
        self.id = None

        # config is the dictionary of configuration options for the widget.
        config = {}
        for option in options:
            config[option] = DEFAULT_CONFIG[option]
        self.config = config

    def set_fill(self, color):
        """Set interior color to color"""
        self._reconfig("fill", color)

    def set_outline(self, color):
        """Set outline color to color"""
        self._reconfig("outline", color)

    def set_width(self, width):
        """Set line weight to width"""
        self._reconfig("width", width)

    def draw(self, graphwin):
        """Draw the object in graphwin, which should be a GraphWin
        object.  A GraphicsObject may only be drawn into one
        window. Raises an error if attempt made to draw an object that
        is already visible.
        """

        if self.canvas and not self.canvas.is_closed():
            raise GraphicsError(OBJ_ALREADY_DRAWN)
        if graphwin.is_closed():
            raise GraphicsError("Can't draw to closed window")
        self.canvas = graphwin
        self.id = self._draw(graphwin, self.config)
        if graphwin.autoflush:
            _root.update()

    def undraw(self):
        """Undraw the object (i.e. hide it). Returns silently if the
        object is not currently drawn.
        """

        if not self.canvas:
            return
        if not self.canvas.is_closed():
            self.canvas.delete(self.id)
            if self.canvas.autoflush:
                _root.update()
        self.canvas = None
        self.id = None

    def move(self, dx, dy):
        """Move object dx units in x direction and dy units in y
        direction
        """

        self._move(dx, dy)
        canvas = self.canvas
        if canvas and not canvas.is_closed():
            trans = canvas.trans
            if trans:
                x = dx / trans.xscale
                y = -dy / trans.yscale
            else:
                x = dx
                y = dy
            self.canvas.move(self.id, x, y)
            if canvas.autoflush:
                _root.update()

    def _reconfig(self, option, setting):
        # Internal method for changing configuration of the object
        # Raises an error if the option does not exist in the config
        #    dictionary for this object
        if option not in self.config:
            raise GraphicsError(UNSUPPORTED_METHOD)
        options = self.config
        options[option] = setting
        if self.canvas and not self.canvas.is_closed():
            self.canvas.itemconfig(self.id, options)
            if self.canvas.autoflush:
                _root.update()

    def _draw(self, canvas, options):
        """Draws appropriate figure on canvas with options provided
        Returns Tk id of item drawn
        """
        pass  # must override in subclass

    def _move(self, dx, dy):
        """Updates internal state of object to move it dx,dy units"""
        pass  # must override in subclass
