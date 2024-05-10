from array import array

""""
    Remove the first occurrence of the specified element from the array
    
    Parameters:
        array_input (arr): Array in which element will get remove
        specified_element (int): Element which will get remove from the array
        
    Returns:
        Return the array with removed first occurrence of the specified element
"""


def remove_first_occurrence(array_input, specified_element):
    index = array_input.index(specified_element)
    array_input.pop(index)

    return array_input


array_input = array('i', [1, 2, 3, 4])
specified_element = int(input("Enter the specified element: "))

if specified_element not in array_input:
    print("Element is not preset in the array")
else:
    print(remove_first_occurrence(array_input, specified_element))
