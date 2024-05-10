"""
    Remove the duplicate elements from the list of lists

    Parameters:
        matrix (2d list): Matrix to which get modify into distinct elements

    Returns:
        Remove the duplicate elements from the List
"""


def remove_duplicates(matrix):
    distinct_matrix = []

    for element in matrix:
        if element not in distinct_matrix:
            distinct_matrix.append(element)

    return distinct_matrix


matrix = [[1, 2], [40], [3, 4], [40]]
print(remove_duplicates(matrix))
