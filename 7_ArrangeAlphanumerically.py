"""
    Sort the comma separated words into a new list

    Parameters:
        string (str): Take the inputs to arrange

    Returns:
        sorted list of the words
"""


def arrange_alphanumerically(string):
    arrange = string.split(", ")

    return sorted(arrange)


comma_separated_words = "green, black, blue, red"
print(arrange_alphanumerically(comma_separated_words))
