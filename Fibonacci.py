"""
    Generate a Fibonacci series up to the specified limit.

    Args:
        limit (int): The upper limit up to which Fibonacci numbers should be generated.

    Returns:
        list: A list containing Fibonacci numbers up to the limit.

    """


def fibonacci_series(limit):
    fibonacci_list = [0, 1]
    a, b = 0, 1

    # Loop to generate Fibonacci numbers up to the limit
    while b < limit:
        temp = a
        a = b
        b = temp + a
        if b <= limit:
            fibonacci_list.append(b)

    return fibonacci_list


limit = int(input("Enter the limit of the fibonacci: "))
fibonacci = fibonacci_series(limit)

print(fibonacci)
