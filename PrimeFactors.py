import math

"""
    Check whether a number is prime or not.

    Args:
        num (int): The number to be checked.

    Returns:
        bool: True if the number is prime, False otherwise.
    """


def check_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


num = int(input("Enter the number: "))
factor = []

for i in range(1, num + 1):
    if num % i == 0 and check_prime(i):
        factor.append(i)
        num = num / i

factor.pop(0)
print(factor)
