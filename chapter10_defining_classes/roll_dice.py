from random import randrange
from chapter0_provided_graphics.graphics import GraphicsWindow, Point
from button import Button
from die import Die


def main():
    window = GraphicsWindow("Dice Roller")
    window.set_coords(0, 0, 10, 10)
    window.set_background("#076324")

    # Draw the interface.
    die1 = Die(window, Point(3, 7), 2)
    die2 = Die(window, Point(7, 7), 2)
    roll_button = Button(window, Point(5, 4.5), 4, 1, "Roll Dice")
    roll_button.set_active_status(True)
    quit_button = Button(window, Point(5, 1), 2, 1, "Quit")
    quit_button.set_active_status(False)

    # Handle the user actions.
    point_clicked = window.get_mouse()
    while not quit_button.clicked(point_clicked):
        if roll_button.clicked(point_clicked):
            value1 = randrange(1, 7)
            die1.set_value(value1)

            value2 = randrange(1, 7)
            die2.set_value(value2)

            quit_button.set_active_status(True)

        point_clicked = window.get_mouse()

    window.close()


if __name__ == "__main__":
    main()
