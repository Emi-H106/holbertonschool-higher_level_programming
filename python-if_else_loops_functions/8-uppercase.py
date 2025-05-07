#!/usr/bin/python3

def uppercase(str):
    result = []

    for char in str:
        if 'a' <= char <= 'z':
            upper_char = chr(ord(char) - 32)
            result.append(upper_char)
        else:
            result.append(char)

    print("{}".format(*result))
