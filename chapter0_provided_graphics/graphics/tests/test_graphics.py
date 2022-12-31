# These classes were originally provided from the textbook and can be found free
# here: https://mcsp.wartburg.edu/zelle/python/ppics2/index.html

from circle import Circle
from graphics_window import GraphicsWindow
from point import Point
from polygon import Polygon
from text import Text
from text_box import TextBox


def test():
    print("Testing graphics")

    # Set up graphics window
    window = GraphicsWindow("Testing Graphics", 600, 600)

    # Draw text box
    text_box = TextBox(Point(200, 300), 30)
    text_box.set_text("Placeholder text . . . ")
    text_box.set_text_color("#333333")
    text_box.draw(window)

    # Draw a circle
    circle = Circle(Point(50, 50), 20)
    circle.draw(window)
    window.get_mouse()  # Pause to view result

    # Display text
    text = Text(Point(400, 400), "Showing off my Text class")
    text.set_font_size(14)
    text.set_font_face("arial")
    text.set_font_style("bold italic")
    text.draw(window)
    window.get_mouse()  # Pause to view result

    # Draw a polygon
    polygon = Polygon(Point(200, 200), Point(250, 100), Point(100, 60))
    polygon.draw(window)
    polygon.set_fill("red")
    polygon.set_outline("blue")
    window.get_mouse()  # Pause to view result

    # Update display text with text input and move text box
    display_text = ""
    for pt in polygon.get_points():
        display_text = display_text + "(%0.1f,%0.1f) " % (pt.get_x(), pt.get_y())
    text.set_text(text_box.get_text())
    text_box.set_fill("green")
    text_box.set_text("Spam!")
    text_box.move(2, 0)
    window.get_mouse()  # Pause to view result

    # Move polygon
    polygon.move(2, 3)
    window.get_mouse()  # Pause to view result

    # Update display text
    display_text = ""
    for point in polygon.get_points():
        display_text = display_text + "(%0.1f,%0.1f) " % (point.get_x(), point.get_y())
    text.set_text(display_text)
    window.get_mouse()  # Pause to view result

    # Undraw items
    polygon.undraw()
    window.get_mouse()  # Pause to view result

    # Close window when done
    window.close()


if __name__ == "__main__":
    test()
