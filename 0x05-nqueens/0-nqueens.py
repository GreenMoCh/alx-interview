#!/usr/bin/python3
"""
N queens
"""

import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at the given position on the board
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def slove_nqueens_util(board, row, N, solutions):
    """
    Recursively slove N queens problem
    """
    if row == N:
        solution = [[r, c] for r in range(N) for c in range(N) if board[r][c] == 1]
        solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            slove_nqueens_util(board, row + 1, N, solutions)
            board[row][col] = 0

def slove_nqueens(N):
    """
    Slove the N queens problem and print the solutions
    """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    slove_nqueens_util(board, 0, N, solutions)

    for solution in solutions:
        print(solution)
