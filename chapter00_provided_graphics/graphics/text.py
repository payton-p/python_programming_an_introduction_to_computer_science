from _config import DEFAULT_CONFIG, BAD_OPTION_ERROR_MESSAGE
from _graphics_error import _GraphicsError
from _graphics_object import _GraphicsObject


class Text(_GraphicsObject):
    """A Text object represents a text graphic that can be drawn."""

    def __init__(self, anchor_point, text):
        """
        Construct a text object that displays the given string centered at the anchor point. The text is displayed
        horizontally.
        """

        _GraphicsObject.__init__(self, ["justify", "fill", "text", "font"])
        self.set_text(text)
        self.anchor = anchor_point.clone()
        self.set_fill(DEFAULT_CONFIG['outline'])
        self.set_outline = self.set_fill

    def clone(self):
        """Return a clone of the object."""

        other = Text(self.anchor, self.config['text'])
        other.config = self.config.copy()

        return other

    def set_text(self, text):
        """Set the value of text."""

        self._reconfig("text", text)

    def get_text(self):
        """Return the value of text."""

        return self.config["text"]

    def get_anchor(self):
        """Return a clone of the anchor point."""

        return self.anchor.clone()

    def set_font_face(self, typeface):
        """
        Change the font face to the given family.

        Possible values are: "helvetica", "courier", "times roman", and "arial".
        """

        if typeface in ['helvetica', 'arial', 'courier', 'times roman']:
            font_face, font_size, font_style = self.config['font']
            self._reconfig("font", (typeface, font_size, font_style))
        else:
            raise _GraphicsError(BAD_OPTION_ERROR_MESSAGE)

    def set_font_size(self, size):
        """
        Change the font size to the given point size.

        Sizes from 5 to 36 are legal.
        """

        if 5 <= size <= 36:
            font_face, font_size, font_style = self.config['font']
            self._reconfig("font", (font_face, size, font_style))
        else:
            raise _GraphicsError(BAD_OPTION_ERROR_MESSAGE)

    def set_font_style(self, style):
        """
        Change font to the given style.

        Possible values are "normal", "bold", "italic", and "bold italic".
        """

        if style in ['bold', 'normal', 'italic', 'bold italic']:
            font_face, font_size, font_style = self.config['font']
            self._reconfig("font", (font_face, font_size, style))
        else:
            raise _GraphicsError(BAD_OPTION_ERROR_MESSAGE)

    def set_text_color(self, color):
        """
        Set the color of the text.

        Note: set_fill has the same effect.
        """

        self.set_fill(color)

    def _draw(self, canvas, options):
        """Draw the object in a GraphicsWindow."""

        point = self.anchor
        x, y = canvas.get_screen_coords(point.x, point.y)

        return canvas.create_text(x, y, options)

    def _move(self, dx, dy):
        """Update internal state of object to move it dx,dy units."""

        self.anchor.move(dx, dy)
