#!/usr/bin/python3
"""
This module contains a function that calculates the minimum number
of operations needed to achieve exactly `n` 'H' characters in a text
file using only "Copy All" and "Paste" operations.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations needed
        to reach n 'H' characters.
             Returns 0 if n is impossible to achieve.
    """
    # If n is less than or equal to 1, it's impossible to achieve, return 0.
    if n <= 1:
        return 0

    # Initialize the operation count.
    operations = 0
    # Start with the smallest factor, which is 2.
    factor = 2

    # Loop to reduce n by its smallest factor repeatedly.
    while n > 1:
        # Check if the current factor can divide n evenly.
        while n % factor == 0:
            # Add the factor to the operation count, as this factor represents
            # the number of Paste operations after a Copy All.
            operations += factor
            # Reduce n by dividing it by the current factor.
            n //= factor
        # Move to the next possible factor.
        factor += 1

    # Return the total number of operations required.
    return operations
