"""
    Find the maximum and minimum value in the set

    Parameters:
        set_input (set): Set in which max and min value to print

    Returns:
        None
"""


def find_max_and_min_in_set(set_input):
    max_num = max(set_input)
    min_num = min(set_input)

    print("Maximum in the set: " + str(max_num))
    print("Minimum in the set: " + str(min_num))


set1 = {2, 3, 4, 2, 3, 4, 3, 2, 2, 544, 4}

find_max_and_min_in_set(set1)
