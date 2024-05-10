my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 5, 'e': 4}

# Will sort the dictionary in ascending by using values
ascending_sort_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(ascending_sort_dict)

# Will sort the dictionary in descending by using values
descending_sort_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print(descending_sort_dict)