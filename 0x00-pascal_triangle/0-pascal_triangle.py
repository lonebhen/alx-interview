#!/usr/bin/python3

"""returns a list of lists of integers representing the Pascal`s triangle"""


def pascal_triangle(n):
    """ Pascal Triangle"""

    if n <= 0:
        return []
    triangles = [[1]]
    while len(triangles) != n:
        last_row = triangles[-1]
        tmp = [1]

        for i in range(len(last_row) - 1):
            tmp.append(last_row[i]+last_row[i+1])
        tmp.append(last_row[-1])
        triangles.append(tmp)
    return triangles
