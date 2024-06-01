#!/usr/bin/python3
"""Island perimeter"""


def ismand_perimeter(grid):
    """
    Calculates the perimeter of an island
    Args:
        grid: second list of ints
    Returns:
        the perimeter of the island
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                if (i <= 0 or grid[i - 1][j] == 0):
                    perimeter = perimeter + 1

                if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                    perimeter = perimeter + 1

                if (j <= 0 or grid[i][j - 1] == 0):
                    perimeter = perimeter + 1

                if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                    perimeter = perimeter + 1

    return perimeter
