#!/usr/bin/python3
"""
This module returna the fewest number of coins needed to meet a given total.
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to make the given total.

    Args:
        coins (list of int): The denominations of the coins available.
        total (int): The total amount to make.

    Returns:
        int: The fewest number of coins needed to make the total.
        If the total is 0 or less, return 0.
        If it's not possible to make the total with the available coins,
        return -1.
    """
    if total <= 0:
        return 0

    # Initialize dp array with "infinity" for all totals > 0 and dp[0] = 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Loop over each coin and update the dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be made
    return dp[total] if dp[total] != float('inf') else -1
