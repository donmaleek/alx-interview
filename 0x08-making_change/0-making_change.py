#!/usr/bin/python3
"""0x19. Making Change"""


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total"""
    if total <= 0:
        return 0

    val = [float('inf')] * (total + 1)
    val[0] = 0

    for i in range(1, len(val)):
        for j in range(len(coins)):
            if coins[j] <= i:
                val[i] = min(val[i], val[i - coins[j]] + 1)

    return val[i] if val[i] != float('inf') else -1
