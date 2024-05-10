my_set = frozenset([1,2,3])

print(my_set)

my_set.add(4) # Will throw an error because frozen sets are immutable
my_set.remove(3) # Throw an error because frozen sets are immutable