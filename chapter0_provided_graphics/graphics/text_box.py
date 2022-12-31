import tkinter

from _config import DEFAULT_CONFIG, BAD_OPTION_ERROR_MESSAGE, _root
from _graphics_error import _GraphicsError
from _graphics_object import _GraphicsObject


class TextBox(_GraphicsObject):
    """Objects of type TextBox are displayed as text boxes, where users can enter input."""

    def __init__(self, anchor_point, width):
        """
        Construct a TextBox having the given center point and width.

        The width is specified as the number of characters that can be displayed.
        """

        _GraphicsObject.__init__(self, [])
        self.anchor = anchor_point.clone()
        self.width = width
        self.text = tkinter.StringVar(_root)
        self.text.set("")
        self.background_color = "white"
        self.text_color = "black"
        self.font_config = DEFAULT_CONFIG['font']
        self.text_box = None

    def get_anchor(self):
        """Return a clone of the anchor point."""

        return self.anchor.clone()

    def clone(self):
        """Return a clone of the object."""

        other = TextBox(self.anchor, self.width)
        other.config = self.config.copy()
        other.text = tkinter.StringVar()
        other.text.set(self.text.get())
        other.background_color = self.background_color

        return other

    def get_text(self):
        """Return the value of text."""

        return self.text.get()

    def set_text(self, t):
        """Set the value of text."""

        self.text.set(t)

    def set_fill(self, color):
        """Set background color."""

        self.background_color = color
        if self.text_box:
            self.text_box.config(bg=color)

    def set_font_face(self, typeface):
        """
        Change the font face to the given family.

        Possible values are: "helvetica", "courier", "times roman", and "arial".
        """

        if typeface in ['helvetica', 'arial', 'courier', 'times roman']:
            self._set_font_config(0, typeface)
        else:
            raise _GraphicsError(BAD_OPTION_ERROR_MESSAGE)

    def set_font_size(self, size):
        """
        Change the font size to the given point size.

        Sizes from 5 to 36 are legal.
        """

        if 5 <= size <= 36:
            self._set_font_config(1, size)
        else:
            raise _GraphicsError(BAD_OPTION_ERROR_MESSAGE)

    def set_font_style(self, style):
        """
        Change font to the given style.

        Possible values are "normal", "bold", "italic", and "bold italic".
        """

        if style in ['bold', 'normal', 'italic', 'bold italic']:
            self._set_font_config(2, style)
        else:
            raise _GraphicsError(BAD_OPTION_ERROR_MESSAGE)

    def set_text_color(self, color):
        """Set the color of the text."""

        self.text_color = color
        if self.text_box:
            self.text_box.config(fg=color)

    def _set_font_config(self, index, value):
        """Set the font config."""

        font_config = list(self.font_config)
        font_config[index] = value
        self.font_config = tuple(font_config)
        if self.text_box:
            self.text_box.config(font=self.font_config)

    def _draw(self, canvas, options):
        """Draw the object in a GraphicsWindow."""

        point = self.anchor
        x, y = canvas.get_screen_coords(point.x, point.y)
        
        frame = tkinter.Frame(canvas.master)
        w = self.width
        text = self.text
        bg_color = self.background_color
        text_color = self.text_color
        font_config = self.font_config
        self.text_box = tkinter.Entry(frame, width=w, textvariable=text, bg=bg_color, fg=text_color, font=font_config)

        self.text_box.pack()
        self.set_fill(self.background_color)

        return canvas.create_window(x, y, window=frame)

    def _move(self, dx, dy):
        """Update internal state of object to move it dx,dy units."""

        self.anchor.move(dx, dy)
