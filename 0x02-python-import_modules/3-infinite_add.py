#!/usr/bin/python3

result = 0
if __name__ == "__main__":
    """Prints the result of the addition of all arguments"""
    from sys import argv

    for i in range(len(argv) - 1):
        result += int(argv[i + 1])
    print("{}".format(result))
