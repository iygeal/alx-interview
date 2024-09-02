#!/usr/bin/python3
"""This module defines a function that determines if a string
is a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): Data set to evaluate.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """

    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 0b10000000  # 128 in decimal
    mask2 = 0b11100000  # 192 in decimal

    for num in data:
        # Get only the least significant 8 bits (simulate 1 byte)
        byte = num & 0xff

        if num_bytes == 0:
            # Determine how many bytes the UTF-8 character has
            if byte & mask1 == 0:
                # 1 byte character
                continue
            elif byte & mask2 == 0b11000000:
                # 2-byte character (110xxxxx)
                num_bytes = 1
            elif byte & 0b11110000 == 0b11100000:
                # 3-byte character (1110xxxx)
                num_bytes = 2
            elif byte & 0b11111000 == 0b11110000:
                # 4-byte character (11110xxx)
                num_bytes = 3
            else:
                # Invalid UTF-8 character
                return False

        else:
            # For subsequent bytes, check if they start with 10xxxxxx
            if byte & 0b11000000 != mask1:
                return False

            num_bytes -= 1

    # If num_bytes is not 0, it means we have an incomplete
    # multi-byte character
    return num_bytes == 0
