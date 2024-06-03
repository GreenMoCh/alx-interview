#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0

    db = [float('inf')] * (total + 1)
    db[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            db[amount] = min(db[amount], db[amount - coin] + 1)

    return db[total] if db[total} != float('inf') else -1
