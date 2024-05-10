"""
    Method to create the tuple from the user input

    Parameters:
        None

    Returns:
        created tuple
"""


def create_tuple():
    elements = input("Enter the elements of the tuple: ").split(",")

    my_tuple = tuple(elements)

    return my_tuple


my_tuple = create_tuple()
print(my_tuple)
