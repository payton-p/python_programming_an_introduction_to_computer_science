from chapter0_provided_graphics.graphics import GraphicsWindow, Point, Rectangle, Text


def main():
    print("This program plots the growth of a 10-year investment.")

    # Get principal and interest rate.
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual percentage rate: "))

    # Create a graphics window with labels on left edge
    window = GraphicsWindow("Investment Growth Chart", 800, 600)
    window.set_background("white")
    window.set_coords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0K').draw(window)
    Text(Point(-1, 2500), ' 2.5K').draw(window)
    Text(Point(-1, 5000), ' 5.0K').draw(window)
    Text(Point(-1, 7500), ' 7.5k').draw(window)
    Text(Point(-1, 10000), '10.0K').draw(window)

    # Draw bar for initial principal
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.set_fill("green")
    bar.set_width(2)
    bar.draw(window)

    # Draw a bar for each subsequent year
    for year in range(1, 11):
        accumulated_value = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year + 1, accumulated_value))
        bar.set_fill("green")
        bar.set_width(2)
        bar.draw(window)
        principal = accumulated_value  # set new principal for the next loop

    # Format the end balance to 2 decimal places. Also, note how the scope is working for accumulated_value. This is
    # unique. Explanation: In Python, for-loops use the scope they exist in and leave their defined loop-variable behind
    # in the surrounding scope. This also applies if we explicitly defined the for-loop variable in the global namespace
    # before. In this case, it will rebind the existing variable.
    print("End balance: ${0:.2f}".format(accumulated_value))

    window.get_mouse()  # Pause to view result
    window.close()


main()
