#!/usr/bin/env python3

"""
    UTF-8 encoding
"""


def validUTF8(data):
    """Validate utf-8 encoding"""
    num_bytes = 0

    for d in data:
        if num_bytes == 0:
            if d >> 7 == 0b0:
                continue
            elif d >> 5 == 0b110:
                num_bytes = 1
            elif d >> 4 == 0b1110:
                num_bytes = 2
            elif d >> 3 == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            if d >> 6 != 0b10:
                return False
            num_bytes -= 1
    return num_bytes == 0


# data = [229, 65, 127, 256]
# print(validUTF8(data))
