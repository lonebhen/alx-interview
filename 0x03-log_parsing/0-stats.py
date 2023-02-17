#!/usr/bin/python3

"""
    a script that reads stdin line by line and computes metrics:
"""
import sys

file_size = 0
code = 0
line_count = 0
codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}


def print_res(codes, file_size):
    print("File size: {}".format(file_size))
    for key, value in sorted(codes.items()):
        print("{}: {}".format(key, value))


try:
    for line in sys.stdin:
        read_line = line.split()

        if len(read_line) > 2:
            line_count += 1

            if line_count <= 10:
                file_size = int(read_line[-1])
                code = read_line[-2]

                if (code in codes.keys()):
                    codes[code] += 1

            if line_count == 10:
                print_res(codes, file_size)
                line_count = 0

finally:
    print_res(codes, file_size)
