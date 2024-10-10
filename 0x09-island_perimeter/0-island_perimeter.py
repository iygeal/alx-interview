#!/usr/bin/python3
"""This module provides the island_perimeter function which returns the
perimeter of the island described in grid.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island in a grid.

    Args:
        grid (list of list of ints): A grid where 1 represents
        land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Add 4 for the land cell
                perimeter += 4

                # Check the cell above (if it exists and is land)
                if r > 0 and grid[r - 1][c] == 1:
                    # Subtract 2 for shared edge with the cell above
                    perimeter -= 2

                # Check the cell to the left (if it exists and is land)
                if c > 0 and grid[r][c - 1] == 1:
                    # Subtract 2 for shared edge with the cell to the left
                    perimeter -= 2

    return perimeter
