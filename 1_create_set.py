"""
    To create the sets from the user input

    Parameters:
        None

    Returns:
        return the set of the user input
"""


def create_sets():
    user_input = input("Enter the values: ").split(",")

    return set(user_input)


print(create_sets())
