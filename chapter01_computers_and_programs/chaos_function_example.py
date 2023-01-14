# "Python creates a companion file with a .pyc extension. This is an intermediate file used by the Python
# interpreter. Technically, Python uses a hybrid compiling/interpreting process. The Python source in the
# module file is compiled into more primitive instructions called byte code. This byte code (the .pyc file)
# is then interpreted." (pg. 14)

# " . . . the chaos program illustrates an interesting phenomenon . . . you'll find that no matter what
# number you start with, the results are always similar: the program spits back 10 seemingly random
# numbers between 0 and 1. As the program runs, the value of x seems to jump around, well, chaotically
# . . . The function computed by this program has the general form: k(x)(1 - x), where k in this case
# is 3.9. This is called a logistic function. It models certain kinds of unstable electronic circuits
# and is also sometimes used to predict population under limiting conditions. Repeated application
# of the logistic function can produce chaos. Although our program has a well-defined underlying behavior,
# the output seems unpredictable." (pg. 18)

# Chaos Theory: Where a tiny error or uncertainty in input measurements can cause a massive error in output,
# this is a chaotic function.


def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)


if __name__ == "__main__":
    main()
