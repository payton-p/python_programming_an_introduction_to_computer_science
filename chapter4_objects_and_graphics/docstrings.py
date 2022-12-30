from chapter0_provided_graphics.graphics import Circle, GraphicsWindow


def multi_line_docstring_example(arg1):
    """
    Summary line.

    Extended description of function.

    Parameters:
    arg1 (int): Description of arg1

    Returns:
    int: Description of return value

    """

    return arg1


def main():
    # Docstrings are similar in spirit to commenting, but they are enhanced, more logical, and useful versions of
    # commenting. Docstrings act as documentation for the class, module, and packages. Unlike conventional source code
    # comments, the docstring should describe what the function does, not how. All functions should have a docstring.
    print("\nGet help info for class/module:")
    help(GraphicsWindow)  # gives details on the entire class

    print("\nGet __doc__ for class:")
    print(GraphicsWindow.__doc__)  # gives the description of the class

    print("\nGet __doc__ for function:")
    print(GraphicsWindow.set_background.__doc__)  # gives the description of the function

    # Example of how a multi-line docstring should be formatted.
    print("\nFormatting example:")
    print(multi_line_docstring_example.__doc__)


main()
