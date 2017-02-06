#!/usr/bin/env python

import sys
import re

escaped = re.compile(r"\\[\"\\]")
hexed = re.compile(r"\\x[0-9a-f]{1,2}")

total_code = 0
total_mem = 0

for line in sys.stdin:
    line = line.strip()

    hexes = hexed.findall(line)
    escapes = escaped.findall(line)

    # for each escaped hex, we subtract 3 from code_count
    # for each escaped char we subtract 1
    # subtract 2 for the surrounding quotes
    code_count = len(line)
    mem_count = code_count - (3 * len(hexes)) - len(escapes) - 2

    total_code += code_count
    total_mem += mem_count

print(total_code - total_mem)
