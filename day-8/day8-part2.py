#!/usr/bin/env python

import sys
import re

escaped = re.compile(r"\\[\"\\]")
hexed = re.compile(r"\\x[0-9a-f]{1,2}")

total_string = 0
total_encoded = 0

for line in sys.stdin:
    line = line.strip()

    string_count = len(line)
    encoded_count = 0

    hexes = hexed.findall(line)
    escapes = escaped.findall(line)

    # for each escaped hex, we add 1
    # for each escaped char we add 2
    # add 4 for the surrounding quotes + new quotes
    encoded_count = string_count + len(hexes) + (2 * len(escapes)) + 4

    total_string += string_count
    total_encoded += encoded_count

print(total_encoded - total_string)
