import math

"""
    Check if a number is prime.

    A prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself.

    Args:
        num_to_check (int): The number to be checked for being prime.

    Returns:
        bool: True if the number is prime, False otherwise.
    """


def check_prime(num_to_check):
    if num_to_check == 1 or num_to_check == 0:
        return False

    for i in range(2, int(math.sqrt(num_to_check) + 1)):
        if num_to_check % i == 0:
            return False

    return True


num = int(input("Enter the number to check for prime: "))

if check_prime(num):
    print("Number is Prime")
else:
    print("Number is not Prime")
