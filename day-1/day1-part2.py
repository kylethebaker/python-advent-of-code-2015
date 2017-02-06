#!/usr/bin/env python

import sys

floor = 0
count = 0
for input in sys.stdin:
    for c in input:
        count += 1
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        if floor < 0:
            break

print(count)
