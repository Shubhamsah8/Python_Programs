"""
    Reverse a given number using integer arithmetic.

    Args:
        number_to_reverse (int): The number to be reversed.

    Returns:
        int: The reversed number.
    """


def reverse_number(number_to_reverse):
    reverse = 0

    while number_to_reverse != 0:
        digit = number_to_reverse % 10
        reverse = reverse * 10 + digit
        number_to_reverse //= 10

    return reverse


"""
    Reverse a given number using string manipulation.

    Args:
        number_to_reverse (int): The number to be reversed.

    Returns:
        int: The reversed number.
    """


def reverse_number_2(number_to_reverse):
    return int(str(number_to_reverse)[::-1])


num = int(input("Enter the number: "))
print(reverse_number(num))
print(reverse_number_2(num))
