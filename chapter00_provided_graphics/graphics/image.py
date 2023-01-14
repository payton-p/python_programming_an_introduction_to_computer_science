import os
import tkinter

from _config import _root
from _graphics_object import _GraphicsObject
from point import Point


class Image(_GraphicsObject):
    """An Image object represents an image graphic that can be drawn."""

    id_count = 0
    image_cache = {}  # tkinter photoimages go here to avoid garbage collection while drawn

    def __init__(self, anchor_point, *pix_map):
        """
        Construct an image from the given file, centered at the given anchor point.

        The second argument can be the filename or width and height parameters. If it's called with width and height
        parameters, a blank (transparent) image is created with the given width and height (in pixels). Simple image
        manipulation is done through the Pixmap class. A Pixmap object allows pixel-level access to an image. Pixmaps
        allow for saving to a file and may be displayed using an Image object.
        """

        _GraphicsObject.__init__(self, [])
        self.anchor = anchor_point.clone()
        self.image_id = Image.id_count
        Image.id_count = Image.id_count + 1

        if len(pix_map) == 1:  # file name provided
            self.img = tkinter.PhotoImage(file=pix_map[0], master=_root)
        else:  # width and height provided
            width, height = pix_map
            self.img = tkinter.PhotoImage(master=_root, width=width, height=height)

    def undraw(self):
        """Undraw the object, i.e., hide it."""

        del self.image_cache[self.image_id]  # allow garbage collection of tkinter photoimage
        _GraphicsObject.undraw(self)

    def get_anchor(self):
        """Return the anchor point."""

        return self.anchor.clone()

    def clone(self):
        """Return a clone of the object."""

        other = Image(Point(0, 0), 0, 0)
        other.img = self.img.copy()
        other.anchor = self.anchor.clone()
        other.config = self.config.copy()

        return other

    def get_width(self):
        """Return the width of the image in pixels."""

        return self.img.width()

    def get_height(self):
        """Return the height of the image in pixels."""

        return self.img.height()

    def get_pixel_color(self, x, y):
        """
        Return a triple (r,g,b) of the red, green, and blue intensities of the pixel at (x,y).

        Intensity values are in range(256).
        """

        rgb_triple = self.img.get(x, y)
        if isinstance(rgb_triple, type(0)):
            return [rgb_triple, rgb_triple, rgb_triple]
        else:
            return list(map(int, rgb_triple))

    def set_pixel_color(self, x, y, color):
        """Set pixel at (x,y) to the given color."""

        self.img.put("{" + color + "}", (x, y))

    def save(self, filename):
        """
        Save the image to a file with the given name.

        The format of the file is determined by the extension on the filename, e.g., .ppm or .gif.
        """

        path, name = os.path.split(filename)
        file_format = name.split(".")[-1]
        self.img.write(filename, format=file_format)

    def _draw(self, canvas, options):
        """Draw the object in a GraphicsWindow."""

        anchor_point = self.anchor
        x, y = canvas.get_screen_coords(anchor_point.x, anchor_point.y)
        self.image_cache[self.image_id] = self.img  # save a reference to avoid garbage collection while drawn

        return canvas.create_image(x, y, image=self.img)

    def _move(self, dx, dy):
        """Update internal state of object to move it dx,dy units."""

        self.anchor.move(dx, dy)
