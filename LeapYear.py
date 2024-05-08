"""
    Check if a given year is a leap year.

    Args:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """


def leap_year_check(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# Taking User input for the year
year = int(input("Enter the year: "))

if leap_year_check(year):
    print("It is a leap year")
else:
    print("It is not a leap year")
