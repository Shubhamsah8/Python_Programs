"""
Function to print the quotient and remainder

Args:
    dividend (int): Take the dividend
    divisor (int): Take the divisor
"""


def compute_quotient_remainder(dividend, divisor):
    quotient = dividend / divisor
    actual_quotient = int(quotient)
    remainder = dividend - (divisor * actual_quotient)

    print(actual_quotient)
    print(remainder)


dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

compute_quotient_remainder(dividend, divisor)
