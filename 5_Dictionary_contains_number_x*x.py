"""
    Python script to genrate and print a  dictionary that contains a number
    between 1 and n in the form of (x, x*x)

    Parameters:
        num (int): Till where the key and value pair should get added in the dictionary

    Returns:
        It will return the updated Dictionary
"""


def print_dictionary(num):
    my_dict = {}

    for key in range(1, num + 1):
        value = key * key
        my_dict[key] = value

    return my_dict


num = int(input("Enter the value of n: "))
print(print_dictionary(num))
