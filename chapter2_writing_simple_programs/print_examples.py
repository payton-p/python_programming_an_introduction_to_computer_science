# Notes: Python uses garbage collection (aka the process of automatic memory management). 

def main():
    print("Shall we look at some examples?")

    # The causes a carriage return (aka newline) 
    print()
    print("The line right above this one is from an empty print statement.\n")

    # The end default is a carriage return (\n), but you can explicitly set it.
    print("This print call shows how you can determine what comes at the end. The default is \\n, " +
          "but we are using k instead", end="k")

    print("\n\nThis", "uses", "the", "separator", "option", sep="*")


main()
