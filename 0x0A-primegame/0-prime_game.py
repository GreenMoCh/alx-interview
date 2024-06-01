#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """
    Maria and Ben are playing a game
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0

    for i in range(2, len(a)):
        for j in range(2, len(a)):
            try:
                a[j * x] = 0
            except (ValueError, IndexError):
                break

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"

    return None

