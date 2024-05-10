"""
    Checking the desired element is present in the tuple or not

    Parameters:
        my_tuple (tuple): Tuple to check in which the item is present or not

        item_to_check (int): The element that we have to check in the tuple

    Returns:
        True if the element present otherwise, false
"""


def check_element_in_tuple(my_tuple, item_to_check):
    if item_to_check in my_tuple:
        return True

    return False


my_tuple = (1, 2, 3, 4, 5)
item_to_remove = int(input("Enter the element to check: "))

if check_element_in_tuple(my_tuple, item_to_remove):
    print("Item exists in the tuple")
else:
    print("Item doesn't exist in the tuple")
