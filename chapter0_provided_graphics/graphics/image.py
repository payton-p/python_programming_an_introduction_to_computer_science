import tkinter as tk
import os
from graphics_object import GraphicsObject
from point import Point
from config import _root


class Image(GraphicsObject):
    idCount = 0
    imageCache = {}  # tk photoimages go here to avoid GC while drawn

    def __init__(self, p, *pixmap):
        GraphicsObject.__init__(self, [])
        self.anchor = p.clone()
        self.imageId = Image.idCount
        Image.idCount = Image.idCount + 1
        if len(pixmap) == 1:  # file name provided
            self.img = tk.PhotoImage(file=pixmap[0], master=_root)
        else:  # width and height provided
            width, height = pixmap
            self.img = tk.PhotoImage(master=_root, width=width, height=height)

    def _draw(self, canvas, options):
        p = self.anchor
        x, y = canvas.to_screen(p.x, p.y)
        self.imageCache[self.imageId] = self.img  # save a reference
        return canvas.create_image(x, y, image=self.img)

    def _move(self, dx, dy):
        self.anchor.move(dx, dy)

    def undraw(self):
        del self.imageCache[self.imageId]  # allow gc of tk photoimage
        GraphicsObject.undraw(self)

    def get_anchor(self):
        return self.anchor.clone()

    def clone(self):
        other = Image(Point(0, 0), 0, 0)
        other.img = self.img.copy()
        other.anchor = self.anchor.clone()
        other.config = self.config.copy()
        return other

    def get_width(self):
        """Returns the width of the image in pixels"""
        return self.img.width()

    def get_height(self):
        """Returns the height of the image in pixels"""
        return self.img.height()

    def get_pixel(self, x, y):
        """Returns a list [r,g,b] with the RGB color values for pixel (x,y)
        r,g,b are in range(256)
        """

        value = self.img.get(x, y)
        if isinstance(value, type(0)):
            return [value, value, value]
        else:
            return list(map(int, value))

    def set_pixel(self, x, y, color):
        """Sets pixel (x,y) to the given color"""
        self.img.put("{" + color + "}", (x, y))

    def save(self, filename):
        """Saves the pixmap image to filename.
        The format for the save image is determined from the filename extension.
        """

        path, name = os.path.split(filename)
        ext = name.split(".")[-1]
        self.img.write(filename, format=ext)