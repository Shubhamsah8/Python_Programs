"""
    To get the union of two sets

    Parameters:
        set1 (set): First set
        set2 (set): Secod set which will get unite with set1

    Returns:
        returns the union of the set
"""


def union_of_sets(set1, set2):
    return set1.union(set2)


set1 = {1, 2, 3}
set2 = {4, 5, 5}

union_set = union_of_sets(set1, set2)
print(union_set)
