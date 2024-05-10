"""
    Script to add the key and value in the dictionary

    Parameters:
        my_dict (dict): Will take the dictionary in which the key and value will get added
        key: Key of the dictionary
        value: Value of that key

    Returns:
        The updated dictionary
"""


def add_key_value(my_dict, key, value):
    my_dict[key] = value
    return my_dict


my_dict = {'a': 3, 'b': 5, 'c': 7}
key = input("Enter the key: ")
value = input("Enter the value: ")

print(add_key_value(my_dict, key, value))
