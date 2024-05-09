"""
    Calculate the elapsed time between two given times.

    Args:
        start_hour (int): The hour of the starting time (0-23).
        start_minute (int): The minute of the starting time (0-59).
        end_hour (int): The hour of the ending time (0-23).
        end_minute (int): The minute of the ending time (0-59).

    Returns:
        str: A string representing the elapsed time in the format "hours : minutes".
    """

def calculate_elapsed_time(start_hour, start_minute, end_hour, end_minute):
    start_time = (start_hour * 60) + start_minute
    end_time = (end_hour * 60) + end_minute

    elapsed_time_in_minutes = end_time - start_time
    elapsed_time_hour = elapsed_time_in_minutes // 60
    elapsed_time_minutes = elapsed_time_in_minutes % 60

    elapsed_time = str(elapsed_time_hour) + " : " + str(elapsed_time_minutes)
    return elapsed_time


start_hour = int(input("Enter the starting hour: "))
start_min = int(input("Enter the starting minute: "))
end_hour = int(input("Enter the end hour: "))
end_min = int(input("Enter the end minute: "))

# Check if the input hours and minutes are within valid ranges
if 0 <= start_hour < 24 and 0 <= end_hour < 24 and 0 <= start_min < 60 and 0 <= end_min < 60:
    elapsed_time = calculate_elapsed_time(start_hour, start_min, end_hour, end_min)
    print(elapsed_time)
else:
    print("Invalid input!")
