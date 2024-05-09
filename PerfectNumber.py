"""
    Check if a number is a perfect number.

    A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).

    Args:
        num (int): The number to be checked for being a perfect number.

    Returns:
        bool: True if the number is a perfect number, False otherwise.
    """


def check_perfect_number(num):
    perfect_list = []

    for i in range(1, num):
        if num % i == 0:
            perfect_list.append(i)

    if sum(perfect_list) == num:
        return True

    return False


num = int(input("Enter the number to check the Perfect number: "))

# Check if num is a perfect number and print the result
if check_perfect_number(num):
    print("It is Perfect number")
else:
    print("It is not Perfect number")
