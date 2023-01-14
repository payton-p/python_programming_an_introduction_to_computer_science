from chapter00_provided_graphics.graphics import GraphicsWindow, Point, Rectangle, Text, TextBox


# Program to convert Celsius to Fahrenheit using a simple GUI.
def main():
    window = GraphicsWindow("Celsius Converter", 400, 300)
    window.set_coords(0.0, 0.0, 3.0, 4.0)

    # Draw the interface.
    Text(Point(1, 3), "Celsius Temperature:").draw(window)
    Text(Point(1, 1), "Fahrenheit Temperature:").draw(window)
    text_box = TextBox(Point(2, 3), 5)
    text_box.set_text("0.0")
    text_box.draw(window)
    output = Text(Point(2, 1), "")
    output.draw(window)
    button = Text(Point(1.5, 2.0), "Convert")
    button.draw(window)
    Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(window)
    window.get_mouse()  # Pause to view result

    # Convert input of Celsius.
    celsius = eval(text_box.get_text())
    fahrenheit = 9.0 / 5.0 * celsius + 32

    # Display output and update button text.
    output.set_text(fahrenheit)
    button.set_text("Quit")

    # Wait for click and then quit.
    window.get_mouse()
    window.close()


if __name__ == "__main__":
    main()
