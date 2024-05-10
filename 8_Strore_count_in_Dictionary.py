"""
    Program to create a dictionary from a string, track the count of the letters from the string

    Parameters:
        string (str): To which the letters and it's count will get stored

    Returns:
        Dictionary with the letters as key and their count as values
"""


def store_letters_count(string):
    my_dict = {}

    for letters in string:
        my_dict[letters] = string.count(letters)

    return my_dict


string = "Hello"

print(store_letters_count(string))
