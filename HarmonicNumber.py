"""
    Calculate the nth harmonic number.

    Harmonic number is the sum of reciprocals of the positive integers up to n.

    Args:
        n (int): The nth value for which the harmonic number is to be calculated.

    Returns:
        float: The nth harmonic number.
    """


def nth_harmonic_number(n):
    sum = 0
    for i in range(1, n + 1):
        sum += (1 / i)

    return sum


#Taking the user input for the Harmonic value
n = int(input("Enter the nth value: "))
harmonic = nth_harmonic_number(n)

print(harmonic)
