"""
    To remove the duplicate elements from the list

    Parameters:
        elements (list): To take the list of items

    Returns:
        Return the distinct list of the elements
"""


def remove_duplicate(elements):
    result = []
    for element in elements:
        if element not in result:
            result.append(element)

    return result


elements = [2, 7, "hello", "shubham", 5, "hello", 7]

remove = remove_duplicate(elements)
print(remove)
