#!/usr/bin/python3

"""
Island Perimeter

"""


def island_perimeter(grid):

    '''
    returns the perimeter of island described in grid
    '''
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # number of adjacent cells that are water or out of bounds
                adj_cells = 0
                if i == 0 or grid[i-1][j] == 0:
                    adj_cells += 1
                if i == rows-1 or grid[i+1][j] == 0:
                    adj_cells += 1
                if j == 0 or grid[i][j-1] == 0:
                    adj_cells += 1
                if j == cols-1 or grid[i][j+1] == 0:
                    adj_cells += 1
                perimeter += adj_cells
    return perimeter
