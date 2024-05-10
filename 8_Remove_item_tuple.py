"""
    Program to remove the desired element from the tuple

    Parameters:
        my_tuple (tuple): Tuple in which modify will happen
        item_to_remove (int): which item to remove from the tuple

    Returns:
        If the item_to_remove is not present in the tuple it will throw an error
        
        Otherwise, it will return the modified tuple
"""


def remove_item_from_tuple(my_tuple, item_to_remove):
    temp_list = list(my_tuple)

    if item_to_remove not in temp_list:
        return "Not in the tuple"

    temp_list = [item for item in temp_list if item != item_to_remove]

    return tuple(temp_list)


my_tuple = (2, 3, 4, 2, 4, 7, 889)
item_to_remove = int(input("Enter the item to remove: "))

print(remove_item_from_tuple(my_tuple, item_to_remove))
