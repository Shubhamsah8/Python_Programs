"""
    Changer the occurrence of first character in a string into '$'

    Parameters:
        string: The string in which the modification will happen

    Return:
        The modified string
"""


def modify_string(string):
    first_char = string[0]

    modified_string = first_char + string[1:].replace(first_char, "$")

    return modified_string


string = "suspicious"
print(modify_string(string))
