#!/usr/bin/python3
"""Implementation of the N queens problem(solution) using backtracking.
 """

import sys


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""

    # Check this column on previous rows
    for i in range(row):
        if (board[i] == col or
                board[i] - i == col - row or
                board[i] + i == col + row):
            return False

    return True


def solve_n_queens(board, row, n, solutions):
    """Solve the N queens problem using backtracking."""

    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens(board, row + 1, n, solutions)


def main():
    """
    Main entry point of the program.

    Checks the number of arguments, checks if the argument is a number,
    checks if N is at least 4, initiates the board,
    solves the N queens problem,
    and prints the solutions.
    """
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if the argument is a number
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initiate the board
    board = [-1] * n
    solutions = []

    # Solve the N queens problem
    solve_n_queens(board, 0, n, solutions)

    # Print the solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
