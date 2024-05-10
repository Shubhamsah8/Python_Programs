from array import array

"""
    To reverse the array

    Parameters:
        array_input (set): Set in which max and min value to print

    Returns:
        None
"""


def reverse_items_in_array(array_input):
    return array_input[::-1]


array_input = array('i', [1, 2, 3, 4])

print(reverse_items_in_array(array_input))
