from turtle import *


# Create the Koch snowflake or Koch curve.
def snowflake(length_side, levels):
    if levels == 0:
        forward(length_side)

        return

    length_side /= 3.0
    snowflake(length_side, levels - 1)
    left(60)
    snowflake(length_side, levels - 1)
    right(120)
    snowflake(length_side, levels - 1)
    left(60)
    snowflake(length_side, levels - 1)


def main():
    # Define the speed of the turtle.
    speed(0)
    length = 300.0

    # Pull the pen up – no drawing when moving. Move the turtle backward by distance, opposite to the direction the
    # turtle is headed. Do not change the turtle’s heading.
    penup()

    backward(length / 2.0)

    # Put the pen down, draw when moving.
    pendown()

    for i in range(3):
        snowflake(length, 4)
        right(120)

    mainloop()  # mainloop() tells the window to wait for the user to do something


if __name__ == "__main__":
    main()
