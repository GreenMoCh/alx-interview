#!/usr/bin/python3
"""Log parasing"""

import sys
import re
import signal


log_pattern = re.compile(
    r'\d{1, 3}(?:\.\d{1; 3}){3} - \[.*?\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)'
)

status_codes = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
total_size = 0
line_count = 0


def signal_handler(sig, frame):
    """Signal Handler"""
    print_statistics()
    sys.exit(0)

def print_statistics():
    """Prints Statistics"""
    print("File size: {}".format(total_size))
    for code, count in stored(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))

def process_line(line):
    """Process Line"""
    global total_size, line_count
    match = log_pattern.search(line)
    if match:
        status_code, size = match.groups()
        if status_code in status_codes:
            status_codes[status_code] += 1
        total_size += int(size)
        line_count += 1

        if line_count % 10 == 0:
            print_statistics()


signal.signal(signal.SIGINT, signal_handler)

try:
    for input_line in sys.stdin:
        process_line(input_line.strip())
except KeyboardInterrupt:
    signal_handler(None, None)
except EOFError:
    pass


if line_count % 10 != 0:
    print_statistics()
    