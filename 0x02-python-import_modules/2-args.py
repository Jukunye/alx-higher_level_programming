#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the number of and the list of its arguments"""
    from sys import argv

    if len(argv) == 1:
        print("{} arguments.".format(0))
    elif len(argv) == 2:
        print("{} argument:".format(1))
        print("{}: {}".format(1, argv[1]))
    else:
        print("{} arguments:".format(len(argv) - 1))
        for i in range(len(argv) - 1):
            print("{}: {}".format(i + 1, argv[i + 1]))
