from array import array

my_array = array('i', [1, 2, 3, 4])

# Printing the array using arrays
print(my_array)

# Printing the array through indexes
for i in range(len(my_array)):
    print("Element at index", i, ": ", my_array[i])

