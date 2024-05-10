"""
    To print the intersected elements from two sets

    Parameters:
        set1 (set): First set
        set2 (set): Second set to check the intersection from

    Returns:
        Intersected set
"""


def intersection_of_sets(set1, set2):
    intersected_set = {}

    for item in set1:
        if item in set2:
            intersected_set.add(item)

    return intersected_set


set1 = {1, 2, 3}
set2 = {4, 5, 6}

intersected_set = intersection_of_sets(set1, set2)

if not intersected_set:
    print("There are no intersected elements present")
else:
    print(intersected_set)

