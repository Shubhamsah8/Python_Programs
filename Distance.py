import math

"""
    Calculate the Euclidean distance between two points (x, y) and the origin (0, 0).

    Args:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.

    Returns:
        float: The Euclidean distance between the point (x, y) and the origin (0, 0).
    """


def euclidean_distance(x, y):
    distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    return distance


x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

distance = euclidean_distance(x, y)
print(distance)
