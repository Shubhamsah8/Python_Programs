"""
    To find the count of the strings that has first and last letter is same in a list

    Parameters:
        items (list): List in which strings are present

    Returns:
        The count of the strings that has first and last letter is same in the list
"""


def count_strings(items):
    count = 0
    for item in items:
        if item[0:1] == item[-1:]:
            count += 1

    return count


items = ["abc", "xyz", "aba", "1221"]
count = count_strings(items)

print(count)
