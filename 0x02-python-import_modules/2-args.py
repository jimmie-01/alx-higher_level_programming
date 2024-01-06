#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv_length = len(sys.argv) - 1

    if argv_length == 0:
        print("0 arguments.")
    elif argv_length == 1:
        print("1 argument:")
        print("{}: {}".format(argv_length, (sys.argv[1])))
    else:
        print("{} arguments:".format(argv_length))
        for item in range(argv_length):
            print("{}: {}".format(item + 1, sys.argv[item + 1]))
