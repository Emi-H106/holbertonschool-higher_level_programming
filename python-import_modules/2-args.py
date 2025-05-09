#!/usr/bin/python3

import sys

def print_arguments():
    argv = sys.argv[1:]
    num_arguments = len(argv)

    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_arguments))

    for i in range(len(argv)):
        print(f"{i + 1}: {argv[i]}")

if __name__ == "__main__":
    print_arguments()
