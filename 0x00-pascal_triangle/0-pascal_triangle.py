#!/usr/bin/python3
"""Module that defines a function that represents Pascal's Triangle"""


def pascal_triangle(n):
    """This function returns a list of lists of integers
        representing the Pascal’s triangle:

    Args:
        n (int): Always an integer

    Returns:
        list: list of lists; returns empty lis if n <= 0
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
