#!/usr/bin/python3
"""
This module provides a function to determine whether it is possible
to unlock all boxes given a list of boxes,
where each box contains a list of keys that can unlock other boxes.
"""


def canUnlockAll(boxes):
    """
    This function determines whether it is possible to unlock all boxes
    given a list of boxes, where each box contains a list of keys that
    can unlock other boxes.

    Parameters:
        boxes (list): A list of lists, where each sublist contains keys
        that can unlock other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    keys = set(boxes[0])

    while keys:
        new_key = keys.pop()
        if new_key < len(boxes) and not unlocked[new_key]:
            unlocked[new_key] = True
            keys.update(boxes[new_key])

    return all(unlocked)
