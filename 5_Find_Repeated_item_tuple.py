"""
    To find the repeated items in the tuple and store it into the dictionary

    Parameters:
        my_tuple (tuple): tuple in which duplicate items will present

    Returns:
        It will return the dictionary in which repeated item as key and their count as values
"""


def find_repeated_item(my_tuple):
    repeated_items = {}

    for item in my_tuple:
        if my_tuple.count(item) > 1:
            repeated_items[item] = my_tuple.count(item)

    return repeated_items


my_tuple = (1, 2, 3, 4, 2, 3, 4, 3, 6, 7, 6)
print(find_repeated_item(my_tuple))
