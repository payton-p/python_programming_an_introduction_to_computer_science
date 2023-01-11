from chapter0_provided_graphics.graphics import GraphicsWindow, Point, Polygon, Text


def main():
    window = GraphicsWindow("Draw a Triangle", 500, 500)
    window.set_coords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points.")
    message.draw(window)

    # Get and draw three vertices of triangle.
    p1 = window.get_mouse()
    p1.draw(window)
    p2 = window.get_mouse()
    p2.draw(window)
    p3 = window.get_mouse()
    p3.draw(window)

    # Use Polygon object to draw the triangle.
    triangle = Polygon(p1, p2, p3)
    triangle.set_fill("peachpuff")
    triangle.set_outline("cyan")
    triangle.draw(window)

    # Wait for another click to exit.
    message.set_text("Click anywhere to quit.")
    window.get_mouse()


if __name__ == "__main__":
    main()
