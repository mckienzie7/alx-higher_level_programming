#!/usr/bin/python3
import sys


def print_board(board):
    """Print the chessboard."""
    for row in board:
        print(" ".join(row))


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == "Q":
            return False
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
    # Check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
    return True


def solve(board, col, n):
    """Solve the N queens problem, starting from column col."""
    # Base case: all queens have been placed
    if col == n:
        print_board(board)
        print()
        return True
    # Try placing a queen in each row in the current column
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"
            solve(board, col + 1, n)
            board[row][col] = "."
    return False


if __name__ == "__main__":
    # Check the command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    # Initialize an empty chessboard
    board = [["."] * n for _ in range(n)]
    # Solve the problem starting from the first column
    solve(board, 0, n)
