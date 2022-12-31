from chapter0_provided_graphics.graphics import Circle, GraphicsWindow, Image, Line, Oval, Point, Polygon, Rectangle, \
    Text, TextBox


# graphics is a package/library provided by the textbook that is a wrapper for Tkinter.
def main():
    # General note: getters/setters = accessors/mutators.
    # Two different variables can refer to the exact same object; changes made to the object through one variable will
    # also be visible to the other. This is called aliasing. This should be avoided.

    # Set up graphics window
    window = GraphicsWindow("Testing Graphics", 600, 600)

    # Add a text box
    text_box = TextBox(Point(200, 300), 30)
    text_box.set_text("Placeholder text . . . ")
    text_box.set_text_color("#333333")
    text_box.set_fill("white")
    text_box.draw(window)
    window.get_mouse()  # Pause to view result

    # Plot some points. Point (0, 0) is the top left corner of the window
    point_a = Point(200, 200)
    point_b = Point(140, 100)
    point_a.draw(window)
    point_b.draw(window)
    print("Point A: (" + str(point_a.get_x()) + ", " + str(point_a.get_y()) + ")")
    print("Point B: (" + str(point_b.get_x()) + ", " + str(point_b.get_y()) + ")")
    window.get_mouse()  # Pause to view result

    # Move the point
    point_a.move(40, 0)
    window.get_mouse()  # Pause to view result

    # Draw a circle and add some text
    circle_center = Point(50, 50)
    circle = Circle(circle_center, 20)
    circle.set_fill("red")
    circle.draw(window)
    text = Text(circle_center, "Red Circle")
    text.draw(window)
    text.set_font_face("times roman")
    text.set_font_size(20)
    text.set_font_style("bold")
    window.get_mouse()  # Pause to view result

    # Clone the object
    blue_circle = circle.clone()  # clone the object to avoid an accidental alias
    blue_circle.set_fill("blue")
    blue_circle.draw(window)
    blue_circle.move(30, 30)
    window.get_mouse()  # Pause to view result

    # Add an image, note tkinter was only working with gif
    image = Image(Point(450, 450), "waterfall.gif")
    image.draw(window)
    window.get_mouse()  # Pause to view result

    # Draw a line segment
    line = Line(Point(20, 30), Point(180, 165))
    line.draw(window)
    window.get_mouse()  # Pause to view result

    # Draw oval
    oval = Oval(Point(200, 200), Point(250, 240))
    oval.draw(window)
    window.get_mouse()  # Pause to view result

    # Draw a polygon
    polygon = Polygon(Point(200, 200), Point(250, 100), Point(100, 60))
    polygon.draw(window)
    polygon.set_fill("green")
    polygon.set_outline("blue")
    window.get_mouse()  # Pause to view result

    #  Draw a rectangle
    rectangle = Rectangle(Point(300, 310), Point(370, 370))
    rectangle.draw(window)
    window.get_mouse()  # Pause to view result

    # Undraw items
    polygon.undraw()
    window.get_mouse()  # Pause to view result

    # Close window when done
    window.close()


main()
