import math

"""
    Calculate the wind chill temperature using the given temperature and wind velocity.

    Args:
        temp (float): The temperature in Fahrenheit.
        velocity (float): The wind velocity in miles per hour.

    Returns:
        float: The wind chill temperature in Fahrenheit.
    """


def calculate_wind_chill(temp, velocity):
    wind_chill = 35.74 + (0.6215 * temp) + (((0.4275 * temp) - 35.75) * math.pow(velocity, 0.16))

    return wind_chill


def main():
    """
        Main function to take user input for temperature and velocity, and calculate wind chill.
    """
    temp = float(input("Enter the temperature: "))
    velocity = float(input("Enter the velocity: "))

    wind_chill = calculate_wind_chill(temp, velocity)
    print(wind_chill)


if __name__ == '__main__':
    main()
