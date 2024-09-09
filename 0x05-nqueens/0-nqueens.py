#!/usr/bin/python3
"""Implementation of the N queens problem(solution) using backtracking.
 """

import sys


def solve_n_queens_optimized(
        row, n, board, solutions, cols, main_diag, anti_diag):
    """
    Recursively solves the N queens problem.

    It takes the following parameters (in order):
    - row: the current row being processed
    - n: the size of the board
    - board: a list of column numbers where the queens are placed
    - solutions: a list of lists of coordinates where the queens are placed
    - cols: a list of booleans representing whether a column is occupied
    - main_diag: a list of booleans representing whether
      a main diagonal is occupied
    - anti_diag: a list of booleans representing whether
      an anti diagonal is occupied

    The function works by backtracking. It tries to place a queen in the
    current row, and for each column, it checks if it is safe to do so.
    If it is safe, it recursively calls itself with the next row, and if
    it has found a solution (i.e., a row has been placed in the last row),
    it adds the solution to the list of solutions. Finally, it resets the
    state of the board and tries the next column. If it has tried all
    columns and no solution has been found, it returns.

    :param row: the current row being processed
    :type row: int
    :param n: the size of the board
    :type n: int
    :param board: a list of column numbers where the queens are placed
    :type board: list
    :param solutions: a list of lists of coordinates where the queens
     are placed
    :type solutions: list
    :param cols: a list of booleans representing whether a column is occupied
    :type cols: list
    :param main_diag: a list of booleans representing whether a main diagonal
     is occupied
    :type main_diag: list
    :param anti_diag: a list of booleans representing whether an anti diagonal
     is occupied
    :type anti_diag: list
    """
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return

    # Check if it is safe to place a queen in the current row
    for col in range(n):
        if cols[col] or main_diag[row - col + n - 1] or anti_diag[row + col]:
            continue  # If it is not safe, skip to the next column

        # If it is safe, place the queen in the current row
        board[row] = col

        cols[col] = True  # Mark the column as occupied
        # Mark the main diagonal as occupied
        main_diag[row - col + n - 1] = True
        anti_diag[row + col] = True  # Mark the anti diagonal as occupied

        # Recursively call the function with the next row
        solve_n_queens_optimized(
            row + 1, n, board, solutions, cols, main_diag, anti_diag)

        cols[col] = False  # Mark the column as unoccupied
        # Mark the main diagonal as unoccupied
        main_diag[row - col + n - 1] = False
        anti_diag[row + col] = False  # Mark the anti diagonal as unoccupied


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
    cols = [False] * n
    main_diag = [False] * (2 * n - 1)
    anti_diag = [False] * (2 * n - 1)

    # Solve the N queens problem
    solve_n_queens_optimized(0, n, board, solutions,
                             cols, main_diag, anti_diag)

    # Print the solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
