import tkinter
import time
from _graphics_error import _GraphicsError
from _transform import _Transform
from point import Point
from _config import _root, CLOSED_WINDOW_ERROR_MESSAGE


class GraphicsWindow(tkinter.Canvas):
    """
    A GraphicsWindow object represents a window on the screen where graphics may be drawn. A program may define any
    number of GraphicsWindow objects. In other words, GraphicsWindow is a top-level  window for displaying graphics.
    """

    def __init__(self, title="Graphics Window", width=200, height=200, autoflush=True):
        """
        Construct a new graphics window for drawing on the screen.

        The parameters are optional. The autoflush parameter, if True causes the window to be immediately updated after
        every drawing operation. If autoflush is False, it allows operations to “batch up” for better efficiency.
        """

        master = tkinter.Toplevel(_root)
        master.protocol("WM_DELETE_WINDOW", self.close)
        tkinter.Canvas.__init__(self, master, width=width, height=height)
        master.resizable(None, None)
        master.lift()

        self.master.title(title)
        self.pack()
        self.foreground = "black"
        self.items = []
        self.mouse_x = None
        self.mouse_y = None
        self.bind("<Button-1>", self._on_click)
        self.height = height
        self.width = width
        self.autoflush = autoflush
        self._mouseCallback = None
        self.transform = None
        self.closed = False

        if autoflush:
            _root.update()

    def __check_open(self):
        """Check that the window is open."""

        if self.closed:
            raise _GraphicsError(CLOSED_WINDOW_ERROR_MESSAGE)

    def set_background(self, color):
        """Set the window background to the given color."""

        self.__check_open()
        self.config(bg=color)
        self.__autoflush()

    def set_coords(self, x1, y1, x2, y2):
        """
        Sets the coordinate system of the window. The lower left corner is (x1,y1) and the upper right corner is
        (x2,y2). All subsequent drawing will be done with respect to the altered coordinate system (except for
        plot_pixel).
        """

        self.transform = _Transform(self.width, self.height, x1, y1, x2, y2)

    def close(self):
        """
        Close the window.

        Once a window is closed, further operations on the window will raise a GraphicsError exception.
        """

        if self.closed:
            return

        self.closed = True
        self.master.destroy()
        self.__autoflush()

    def is_closed(self):
        """Return a Boolean indicating if the window has been closed."""

        return self.closed

    def is_open(self):
        """Return a Boolean indicating if the window is open."""

        return not self.closed

    def __autoflush(self):
        """
        Cause any pending window operations to be performed.

        Normally, this will happen automatically during idle periods. Explicit update() calls may be useful for
        animations. If autoflush is True, it causes the window to be immediately updated after every drawing operation.
        If autoflush is False, it allows operations to “batch up” for better efficiency.
        """

        if self.autoflush:
            _root.update()

    def plot(self, x, y, color="black"):
        """
        Draw the pixel at (x, y) in the window.

        Note: pixel-level operations are very inefficient and this method should be avoided.
        """

        self.__check_open()
        xs, ys = self.get_screen_coords(x, y)  # the "s" in xs is referencing the x screen coordinate, same for y
        self.create_line(xs, ys, xs + 1, ys, fill=color)
        self.__autoflush()

    def plot_pixel(self, x, y, color="black"):
        """
        Draw the pixel at the “raw” position (x, y) ignoring any coordinate transformations set up by set_coords.

        Note: pixel-level operations are very inefficient and this method should be avoided.
        """

        self.__check_open()
        self.create_line(x, y, x + 1, y, fill=color)
        self.__autoflush()

    def flush(self):
        """Update drawing to the window."""

        self.__check_open()
        self.update_idletasks()

    def get_mouse(self):
        """
        Pause for the user to click on the window and return where the mouse was clicked as a Point object.

        Raises GraphicsError if the window is closed while get_mouse is in progress.
        """

        self.update()  # flush any prior clicks
        self.mouse_x = None
        self.mouse_y = None
        while self.mouse_x is None or self.mouse_y is None:
            self.update()
            if self.is_closed():
                raise _GraphicsError(CLOSED_WINDOW_ERROR_MESSAGE)
            time.sleep(.1)  # give up thread

        x, y = self.get_world_coords(self.mouse_x, self.mouse_y)
        self.mouse_x = None
        self.mouse_y = None

        return Point(x, y)

    def check_mouse(self):
        """Return last mouse click or None if mouse has not been clicked since last call."""

        if self.is_closed():
            raise _GraphicsError(CLOSED_WINDOW_ERROR_MESSAGE)

        self.update()
        if self.mouse_x is not None and self.mouse_y is not None:
            x, y = self.get_world_coords(self.mouse_x, self.mouse_y)
            self.mouse_x = None
            self.mouse_y = None

            return Point(x, y)
        else:
            return None

    def get_height(self):
        """Return the height of the window."""

        return self.height

    def get_width(self):
        """Return the width of the window."""

        return self.width

    def get_screen_coords(self, x, y):
        """Get the screen (actual window) coordinates."""

        if self.transform:
            return self.transform.get_screen_coords(x, y)
        else:
            return x, y

    def get_world_coords(self, x, y):
        """
        Get the world coordinates.

        World Coordinates: The positions of collections of points (objects) relative to a single shared standard
        zero point. Also known as the "universe" or sometimes "model" coordinate system. This is the base reference
        system for the overall model, (generally in 3D), to which all other model coordinates relate.
        """

        if self.transform:
            return self.transform.get_world_coords(x, y)
        else:
            return x, y

    def _on_click(self, event):
        """Define the on click event behavior."""

        self.mouse_x = event.x
        self.mouse_y = event.y
        if self._mouseCallback:
            self._mouseCallback(Point(event.x, event.y))
