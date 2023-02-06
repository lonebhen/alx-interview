#!/usr/bin/python3

"""Lockboxes problem"""


def canUnlockAll(boxes):
    """Checking if all boxes can be unlocked"""
    unlocked = [0]

    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False


# boxes = [[1], [2], [3], [4], []]
# print(canUnlockAll(boxes))

# boxes1 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# print(canUnlockAll(boxes1))

# boxes2 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes2))
