from _graphics_object import _GraphicsObject
from _graphics_error import _GraphicsError
from _config import DEFAULT_CONFIG, BAD_OPTION_ERROR_MESSAGE


class Text(_GraphicsObject):
    def __init__(self, p, text):
        _GraphicsObject.__init__(self, ["justify", "fill", "text", "font"])
        self.set_text(text)
        self.anchor = p.clone()
        self.set_fill(DEFAULT_CONFIG['outline'])
        self.set_outline = self.set_fill

    def _draw(self, canvas, options):
        p = self.anchor
        x, y = canvas.to_screen(p.x, p.y)

        return canvas.create_text(x, y, options)

    def _move(self, dx, dy):
        self.anchor.move(dx, dy)

    def clone(self):
        other = Text(self.anchor, self.config['text'])
        other.config = self.config.copy()

        return other

    def set_text(self, text):
        self._reconfig("text", text)

    def get_text(self):
        return self.config["text"]

    def get_anchor(self):
        return self.anchor.clone()

    def set_face(self, face):
        if face in ['helvetica', 'arial', 'courier', 'times roman']:
            f, s, b = self.config['font']
            self._reconfig("font", (face, s, b))
        else:
            raise _GraphicsError(BAD_OPTION_ERROR_MESSAGE)

    def set_size(self, size):
        if 5 <= size <= 36:
            f, s, b = self.config['font']
            self._reconfig("font", (f, size, b))
        else:
            raise _GraphicsError(BAD_OPTION_ERROR_MESSAGE)

    def set_style(self, style):
        if style in ['bold', 'normal', 'italic', 'bold italic']:
            f, s, b = self.config['font']
            self._reconfig("font", (f, s, style))
        else:
            raise _GraphicsError(BAD_OPTION_ERROR_MESSAGE)

    def set_text_color(self, color):
        self.set_fill(color)
