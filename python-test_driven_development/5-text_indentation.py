#!/usr/bin/python3

def text_indentation(text):
    """
    The text_indentation function takes a string as input and prints it with two newlines added after each occurrence of the characters ., ?, and :.

    Parameters:
    text (str): The input string to be processed.

    Raises:
    TypeError: If the input text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0
    n = len(text)

    while i < n:
        result += text[i]
        if text[i] in '.?:':
            result += '\n\n'
            i += 1
            while i < n and text[i] == ' ':
                i += 1
            continue
        i += 1

    lines = result.split('\n')
    lines = [line.strip() for line in lines]
    output = '\n'.join(lines)

    print(output, end='')
