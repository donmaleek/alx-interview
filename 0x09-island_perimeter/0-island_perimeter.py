#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """returns the perimeter of the island"""

    ip = 0
    for m in range(len(grid)):
        for n in range(len(grid[m])):
            if (grid[m][n] == 1):
                if (m <= 0 or grid[m - 1][n] == 0):
                    ip += 1
                if (m >= len(grid) - 1 or grid[m + 1][n] == 0):
                    ip += 1
                if (n <= 0 or grid[m][n - 1] == 0):
                    ip += 1
                if (n >= len(grid[m]) - 1 or grid[m][n + 1] == 0):
                    ip += 1
    return ip
