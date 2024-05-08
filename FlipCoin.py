import random


def flip_coin(num_of_flips):
    """
    Simulates flipping a coin a specified number of times and prints the percentage of heads and tails.

    Args:
        num_of_flips (int): The number of times to flip the coin.

    Returns:
        None
    """

    if num_of_flips <= 0:
        print("Please enter only positive integers")
        return

    head = 0
    tail = 0

    for flips in range(num_of_flips):
        if random.random() < 0.5:
            tail += 1
        else:
            head += 1

    head_percentage = (head / num_of_flips) * 100
    tail_percentage = 100 - head_percentage

    print(f"Heads Percentage : {head_percentage:0.2f}")
    print(f"Tails Percentage : {tail_percentage:0.2f}")


# Taking the user input of the number of flips
num_of_flips = int(input("Enter the number of flips of coin: "))
flip_coin(num_of_flips)
