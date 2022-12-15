# These classes were originally provided from the textbook and can be found free
# here: https://mcsp.wartburg.edu/zelle/python/ppics2/index.html

from graphics_window import GraphicsWindow
from point import Point
from text import Text
from text_box import TextBox
from polygon import Polygon
from circle import Circle
from config import _root


def update():
    _root.update()


def color_rgb(r, g, b):
    """r,g,b are intensities of red, green, and blue in range(256)
    Returns color specifier string for the resulting color
    """
    return "#%02x%02x%02x" % (r, g, b)


def test():
    print("Testing graphics")

    # Set up graphics window
    window = GraphicsWindow("Testing Graphics", 400, 400)

    # Draw a circle
    circle = Circle(Point(50, 50), 20)
    circle.draw(window)
    window.get_mouse()  # Pause to view result

    # Display text
    text = Text(Point(100, 100), "Showing off my Text class")
    text.draw(window)
    window.get_mouse()  # Pause to view result

    # Draw a polygon
    polygon = Polygon(Point(200, 200), Point(250, 100), Point(100, 60))
    polygon.draw(window)
    window.get_mouse()  # Pause to view result

    # Draw input field
    text_box = TextBox(Point(200, 300), 30)
    text_box.set_text("Placeholder text . . . ")
    text_box.set_text_color("#333333")
    text_box.set_fill("white")
    text_box.draw(window)
    window.get_mouse()  # Pause to view result

    # Close window when done
    window.close()

    # p.set_fill("red")
    # p.set_outline("blue")
    # p.set_width(2)
    # s = ""
    # for pt in p.get_points():
    #     s = s + "(%0.1f,%0.1f) " % (pt.get_x(), pt.get_y())
    # text.set_text(e.get_text())
    # e.set_fill("green")
    # e.set_text("Spam!")
    # e.move(2, 0)
    # window.get_mouse()
    # p.move(2, 3)
    # s = ""
    # for pt in p.get_points():
    #     s = s + "(%0.1f,%0.1f) " % (pt.get_x(), pt.get_y())
    # text.set_text(s)
    # window.get_mouse()
    # p.undraw()
    # e.undraw()
    # text.set_style("bold")
    # window.get_mouse()
    # text.set_style("normal")
    # window.get_mouse()
    # text.set_style("italic")
    # window.get_mouse()
    # text.set_style("bold italic")
    # window.get_mouse()
    # text.set_size(14)
    # window.get_mouse()
    # text.set_face("arial")
    # text.set_size(20)
    #
    # window.get_mouse()
    # window.close()


if __name__ == "__main__":
    test()
