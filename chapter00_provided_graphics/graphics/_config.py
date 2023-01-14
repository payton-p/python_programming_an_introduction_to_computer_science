import tkinter

_root = tkinter.Tk()
_root.withdraw()

BAD_OPTION_ERROR_MESSAGE = "Illegal option value."
CLOSED_WINDOW_ERROR_MESSAGE = "Window is closed."
DEAD_THREAD_ERROR_MESSAGE = "Graphics thread quit unexpectedly."
OBJ_ALREADY_DRAWN_ERROR_MESSAGE = "Object currently drawn."
UNSUPPORTED_METHOD_ERROR_MESSAGE = "Object doesn't support operation."

# Default values for various item configuration options. Only a subset of keys may be present in the configuration
# dictionary for a given item.
DEFAULT_CONFIG = {
    "fill": "",
    "outline": "black",
    "width": "1",
    "arrow": "none",
    "text": "",
    "justify": "center",
    "font": ("helvetica", 12, "normal")
}
