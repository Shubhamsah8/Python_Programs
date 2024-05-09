import random

"""
    Generate a specified number of unique coupon codes, each with a specified number of digits.

    Args:
        num (int): The number of distinct coupons to generate.
        coupon_digits (int): The number of digits in each coupon code.

    Returns:
        set: A set containing the generated unique coupon codes.
    """


def generate_coupons(num, coupon_digits):
    coupons = set()
    range = 10 ** (coupon_digits - 1)

    while len(coupons) < num:
        random_coupon = random.randint(range, range * 10)
        coupons.add(random_coupon)

    return coupons


num_of_coupons = int(input("Enter the numbr of distinct coupons: "))
coupon_digits = int(input("Enter the number of digits in a coupon: "))

coupons = generate_coupons(num_of_coupons, coupon_digits)
print(coupons)
