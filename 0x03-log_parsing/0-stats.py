#!/usr/bin/python3
"""
This script reads lines from standard input and computes metrics
based on specific patterns in the input data.
It calculates the total file size and counts occurrences of various
HTTP status codes.

Metrics are printed every 10 lines or upon receiving a keyboard
interruption (CTRL + C).
"""

import sys


def print_stats(total_size, status_codes):
    """
    Prints the accumulated metrics including total file size and
    the number of occurrences of each HTTP status code.

    Args:
        total_size (int): The total file size accumulated.
        status_codes (dict): A dictionary
        mapping status codes to their counts.
    """
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))


def process_line(line, total_size, status_codes):
    """
    Processes a single line of input, extracting
    the file size and status code.
    Updates the total size and status code counts accordingly.

    Args:
        line (str): The input line to process.
        total_size (int): The current total file size.
        status_codes (dict): A dictionary mapping status codes
        to their counts.

    Returns:
        tuple: Updated total_size and status_codes.
    """
    try:
        line_list = line.split(" ")
        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            if status_code in status_codes:
                status_codes[status_code] += 1

            total_size += file_size

    except (IndexError, ValueError):
        # Skip the line if it doesn't have the expected format
        pass

    return total_size, status_codes


def main():
    """
    Main function to execute the log parsing script.
    Reads input line by line, processes each line, and periodically
    prints the metrics.
    """
    total_size = 0
    status_codes = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            total_size, status_codes = process_line(
                line, total_size, status_codes)
            line_count += 1

            # Print statistics every 10 lines
            if line_count == 10:
                print_stats(total_size, status_codes)
                line_count = 0

    except KeyboardInterrupt:
        # Print stats on keyboard interruption
        print_stats(total_size, status_codes)
        raise

    finally:
        # Print final stats after finishing reading input
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
