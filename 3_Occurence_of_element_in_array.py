from array import array

"""
    To find the occurrences of the element in the array and storing into the dictionary 
    
    Parameters:
        array_input (array): Array in which the items need to find the occurrences
        
    Returns:
        Will return the dictionary in which store the element and its occurrences
"""


def find_occurrences_of_element(array_input):
    occurrences_of_element = {}

    for item in array_input:
        if item in occurrences_of_element:
            occurrences_of_element[item] += 1
        else:
            occurrences_of_element[item] = 1

    return occurrences_of_element


array_input = array('i', [1, 2, 3, 3, 4, 5, 5, 3])

print(find_occurrences_of_element(array_input))
