#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    sum = 0
    for number in range(len(sys.argv) - 1):
        sum += int(sys.argv[number + 1])
    print("{}".format(sum))

