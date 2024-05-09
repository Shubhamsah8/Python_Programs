import math

"""
    Find the roots of a quadratic equation of the form ax^2 + bx + c = 0.

    Args:
        a (float): Coefficient of x^2.
        b (float): Coefficient of x.
        c (float): Constant term.

    Returns:
        list of float: A list containing the roots of the quadratic equation.
    """


def find_quadratic(a, b, c):
    delta = (math.pow(b, 2)) - (4 * a * c)

    if (delta <0):
        print("Please enter valid values")
        return
    else:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)

    roots = [root1, root2]
    return roots


def main():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))

    roots = find_quadratic(a, b, c)
    print(roots)


if __name__ == '__main__':
    main()
