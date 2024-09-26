#!/usr/bin/python3
"""
Rotate a 2D matrix 90 degrees clockwise in place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates the matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): 2D matrix to rotate.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix (swap elements at (i, j) with (j, i))
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
