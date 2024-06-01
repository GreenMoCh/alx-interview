#!/usr/bin/python3
"""Change comes from within"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0

    db = [total + 1] * (total + 1)
    db[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            db[amount] = min(db[amount], db[amount - coin] + 1)

    if db[total] <= total:
        return db[total]
    else:
        return -1