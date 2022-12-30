import tkinter as tk
from _graphics_object import _GraphicsObject
from _graphics_error import _GraphicsError
from _config import DEFAULT_CONFIG, BAD_OPTION_ERROR_MESSAGE, _root


class TextBox(_GraphicsObject):
    def __init__(self, point, width):
        _GraphicsObject.__init__(self, [])
        self.anchor = point.clone()
        self.width = width
        self.text = tk.StringVar(_root)
        self.text.set("")
        self.fill = "gray"
        self.color = "black"
        self.font = DEFAULT_CONFIG['font']
        self.text_box = None

    def _draw(self, canvas, options):
        p = self.anchor
        x, y = canvas.get_screen_coords(p.x, p.y)
        frm = tk.Frame(canvas.master)
        self.text_box = tk.Entry(frm, width=self.width, textvariable=self.text, bg=self.fill, fg=self.color,
                                 font=self.font)
        self.text_box.pack()
        self.set_fill(self.fill)

        return canvas.create_window(x, y, window=frm)

    def get_text(self):
        return self.text.get()

    def _move(self, dx, dy):
        self.anchor.move(dx, dy)

    def get_anchor(self):
        return self.anchor.clone()

    def clone(self):
        other = TextBox(self.anchor, self.width)
        other.config = self.config.copy()
        other.text = tk.StringVar()
        other.text.set(self.text.get())
        other.fill = self.fill

        return other

    def set_text(self, t):
        self.text.set(t)

    def set_fill(self, color):
        self.fill = color
        if self.text_box:
            self.text_box.config(bg=color)

    def _set_font_component(self, which, value):
        font = list(self.font)
        font[which] = value
        self.font = tuple(font)
        if self.text_box:
            self.text_box.config(font=self.font)

    def set_face(self, face):
        if face in ['helvetica', 'arial', 'courier', 'times roman']:
            self._set_font_component(0, face)
        else:
            raise _GraphicsError(BAD_OPTION_ERROR_MESSAGE)

    def set_size(self, size):
        if 5 <= size <= 36:
            self._set_font_component(1, size)
        else:
            raise _GraphicsError(BAD_OPTION_ERROR_MESSAGE)

    def set_style(self, style):
        if style in ['bold', 'normal', 'italic', 'bold italic']:
            self._set_font_component(2, style)
        else:
            raise _GraphicsError(BAD_OPTION_ERROR_MESSAGE)

    def set_text_color(self, color):
        self.color = color
        if self.text_box:
            self.text_box.config(fg=color)
