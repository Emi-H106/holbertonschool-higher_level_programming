#!/usr/bin/python3
def pow(a, b):
    result = 1
    is_negative = b < 0

    if is_negative:
        b = -b

    for _ in range(b):
        result *= a

    if is_negative:
        result = 1 / result

    return result
