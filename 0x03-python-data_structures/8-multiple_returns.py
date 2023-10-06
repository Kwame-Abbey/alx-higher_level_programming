#!/usr/bin/python3


def multiple_returns(sentence):
    """returns a tuple with the length of a string
    and its first character.
    """
    first_character = ""
    string_len = len(sentence)
    if string_len == 0:
        first_character = None
    else:
        first_character = sentence[0]

    final = (string_len, first_character)
    return final
