#!/usr/bin/python3
"""This module simulates a prime game and determines the winner."""


def sieve_of_eratosthenes(n):
    """Returns a list indicating if numbers <= n are prime."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    # Loop through all numbers from 2 to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            # Mark all multiples of i as non-prime
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve


def isWinner(x, nums):
    """
    Determines the winner after x rounds of the game.

    Args:
        x (int): The number of rounds.
        nums (list): A list of integers,
        where each integer represents n for that round.

    Returns:
        str: The name of the player with the most wins ("Maria" or "Ben")
        or None if it's a tie.
    """
    if x <= 0 or not nums:
        return None

    # Find the maximum number n to generate primes up to the largest n in nums
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # To track the number of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count the number of primes up to n
        prime_count = sum(primes[2:n+1])

        # If the prime count is odd,
        # Maria wins (she goes first), otherwise Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
