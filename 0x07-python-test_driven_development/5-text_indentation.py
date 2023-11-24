#!/usr/bin/python3
'''Text indentation.'''


def text_indentation(text):
    '''
    Method for adding 2 lines after '.?:' chars.

    Args:
        text: The string text.

    Raises:
        TypeError: If text is not a string.
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join([line.strip(" ") for line in text.split(delim)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
