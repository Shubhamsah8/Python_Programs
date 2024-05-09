"""
    Print the characters before the specified character

    Parameters:
        string (str): String which will get modified
        specified_character (str): character that will modify the string

    Returns:
        Will return the modified string
"""


def get_char_before_specified_character(string, specified_character):
    for i in range(len(string)):
        if string[i] == specified_character:
            return string[0:i]


string = "https://www.w3resource.com/python-exercises"
specified_character = "-"

print(get_char_before_specified_character(string, specified_character))