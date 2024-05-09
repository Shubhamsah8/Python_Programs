import random

"""
    Simulate a gambling session and track the number of wins, losses,
    remaining money, win percentage, and loss percentage.

    Parameters:
        stake (int): The initial amount of money the gambler starts with.
        goal (int): The amount of money the gambler aims to reach.

    Returns:
        None
    """


def gamble_track(stake, goal):
    total_wins = 0
    total_loss = 0

    money = stake
    bets = 0

    while 0 < money < goal:
        bets += 1

        # Randomly decide if the gambler wins or loses
        if random.choice([True, False]):
            money += 1
            total_wins += 1
        else:
            money -= 1
            total_loss += 1

    win_percentage = (total_wins / bets) * 100
    loss_percentage = 100 - win_percentage

    print("Number of wins: " + str(total_wins))
    print("Remaining Money: " + str(money))
    print("Win Percentage: " + str(win_percentage))
    print("Loss Percentage: " + str(loss_percentage))


stake = int(input("Enter the stake: "))
goal = int(input("Enter the goal: "))

gamble_track(stake, goal)
