"""
    Find all unique triplets in the given array whose sum is zero.

    Args:
        arr (list of int): The input array.

    Returns:
        list of list: A list containing all unique triplets whose sum is zero.
    """


def find_triplets(arr):
    triplets = []
    n = len(arr)

    # Iterate through each element in the array, using three nested loops to find triplets
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplet = [arr[i], arr[j], arr[k]]
                    triplet.sort()

                    if triplet not in triplets:
                        triplets.append(triplet)

    return triplets


num = int(input("Enter the number of integer: "))
arr = []

for i in range(num):
    element = int(input(f"Enter the {i + 1} element: "))
    arr.append(element)

triplets = find_triplets(arr)
print(triplets)
