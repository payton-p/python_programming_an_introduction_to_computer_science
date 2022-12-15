import tkinter as tk
import time
from graphics_error import GraphicsError
from transform import Transform
from point import Point
from config import _root


class GraphicsWindow(tk.Canvas):
    """A GraphWin is a toplevel window for displaying graphics."""

    def __init__(self, title="Graphics Window", width=200, height=200, autoflush=True):
        master = tk.Toplevel(_root)
        master.protocol("WM_DELETE_WINDOW", self.close)
        tk.Canvas.__init__(self, master, width=width, height=height)
        self.master.title(title)
        self.pack()
        master.resizable(None, None)
        self.foreground = "black"
        self.items = []
        self.mouseX = None
        self.mouseY = None
        self.bind("<Button-1>", self._on_click)
        self.height = height
        self.width = width
        self.autoflush = autoflush
        self._mouseCallback = None
        self.trans = None
        self.closed = False
        master.lift()
        if autoflush:
            _root.update()

    def __check_open(self):
        if self.closed:
            raise GraphicsError("window is closed")

    def set_background(self, color):
        """Set background color of the window"""
        self.__check_open()
        self.config(bg=color)
        self.__autoflush()

    def set_coords(self, x1, y1, x2, y2):
        """Set coordinates of window to run from (x1,y1) in the
        lower-left corner to (x2,y2) in the upper-right corner.
        """
        self.trans = Transform(self.width, self.height, x1, y1, x2, y2)

    def close(self):
        """Close the window"""

        if self.closed:
            return
        self.closed = True
        self.master.destroy()
        self.__autoflush()

    def is_closed(self):
        return self.closed

    def is_open(self):
        return not self.closed

    def __autoflush(self):
        if self.autoflush:
            _root.update()

    def plot(self, x, y, color="black"):
        """Set pixel (x,y) to the given color"""
        self.__check_open()
        xs, ys = self.to_screen(x, y)
        self.create_line(xs, ys, xs + 1, ys, fill=color)
        self.__autoflush()

    def plot_pixel(self, x, y, color="black"):
        """Set pixel raw (independent of window coordinates) pixel
        (x,y) to color
        """
        self.__check_open()
        self.create_line(x, y, x + 1, y, fill=color)
        self.__autoflush()

    def flush(self):
        """Update drawing to the window"""
        self.__check_open()
        self.update_idletasks()

    def get_mouse(self):
        """Wait for mouse click and return Point object representing
        the click
        """
        self.update()  # flush any prior clicks
        self.mouseX = None
        self.mouseY = None
        while self.mouseX is None or self.mouseY is None:
            self.update()
            if self.is_closed():
                raise GraphicsError("get_mouse in closed window")
            time.sleep(.1)  # give up thread
        x, y = self.to_world(self.mouseX, self.mouseY)
        self.mouseX = None
        self.mouseY = None
        return Point(x, y)

    def check_mouse(self):
        """Return last mouse click or None if mouse has
        not been clicked since last call
        """
        if self.is_closed():
            raise GraphicsError("check_mouse in closed window")
        self.update()
        if self.mouseX is not None and self.mouseY is not None:
            x, y = self.to_world(self.mouseX, self.mouseY)
            self.mouseX = None
            self.mouseY = None
            return Point(x, y)
        else:
            return None

    def get_height(self):
        """Return the height of the window"""
        return self.height

    def get_width(self):
        """Return the width of the window"""
        return self.width

    def to_screen(self, x, y):
        trans = self.trans
        if trans:
            return self.trans.screen(x, y)
        else:
            return x, y

    def to_world(self, x, y):
        trans = self.trans
        if trans:
            return self.trans.world(x, y)
        else:
            return x, y

    def set_mouse_handler(self, func):
        self._mouseCallback = func

    def _on_click(self, e):
        self.mouseX = e.x
        self.mouseY = e.y
        if self._mouseCallback:
            self._mouseCallback(Point(e.x, e.y))
