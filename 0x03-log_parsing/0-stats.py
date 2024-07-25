#!/usr/bin/python3
"""Reads from standard input and computes metrics."""

import sys

def print_stats(size, status_codes):
    """Print accumulated metrics.
    
    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

def main():
    size = 0
    status_codes = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 0  # Reset the line count after printing stats
            
            # Process the line
            line = line.strip().split()
            if len(line) >= 6 and line[1] == '-' and line[2].startswith('[') and line[3].endswith(']') and line[4] == '"GET' and line[5] == '/projects/260':
                try:
                    status_code = line[-2]
                    file_size = int(line[-1])
                    if status_code in status_codes:
                        status_codes[status_code] += 1
                    size += file_size
                except (IndexError, ValueError):
                    pass
            
            count += 1
        
        # Print final statistics
        print_stats(size, status_codes)

    except (KeyboardInterrupt, BrokenPipeError):
        # Handle interruption gracefully
        print_stats(size, status_codes)
        sys.exit(0)

if __name__ == "__main__":
    main()
