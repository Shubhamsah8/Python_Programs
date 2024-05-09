def modify_string(string):
    """
    Modify a given string according to certain conditions.

    Parameters:
    string (str): The input string to be modified.

    Returns:
    str: The modified string.
    """
    # Check if the length of the string is less than 3
    if len(string) < 3:
        return string
    else:
        if string[-3:] == "ing":
            return string + "ly"
        else:
            return string + "ing"

# Test the function with a sample string
sentence = "flying"
print(modify_string(sentence))
