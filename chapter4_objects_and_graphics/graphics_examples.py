# The graphics package needs to be added to the interpreter path if it's not being recognized
from graphics import GraphicsWindow, Circle, Point


# graphics is a package/library provided by the textbook that
# is a wrapper for Tkinter.
def main():
    # Set up graphics window
    window = GraphicsWindow("Testing Graphics", 600, 600)

    # Draw a circle
    circle = Circle(Point(50, 50), 20)
    circle.draw(window)
    window.get_mouse()  # Pause to view result

    # Close window when done
    window.close()


main()
