#!/usr/bin/python3

import sys


def sum_arguments():
    args = sys.argv[1:]

    total = sum(int(arg) for arg in args)

    print(total)


if __name__ == "__main__":
    sum_arguments()
