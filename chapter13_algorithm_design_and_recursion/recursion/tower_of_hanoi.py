# This is an elegant solution, but the algorithm belongs to a class known as intractable problems. These are problems
# that require too much computing power (either time or memory) to be solved in practice, except for the simplest cases.
def move_tower(n, source, destination, temp):
    if n == 1:
        print("Move disk from", source, "to", destination + ".")
    else:
        move_tower(n - 1, source, temp, destination)
        move_tower(1, source, destination, temp)
        move_tower(n - 1, temp, destination, source)


def main():
    print("Tower of Hanoi")
    n = eval(input("How many disks?: "))
    move_tower(n, "A", "C", "B")


if __name__ == '__main__':
    main()
