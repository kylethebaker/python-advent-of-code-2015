#!/usr/bin/env python

import sys

total = 0
for line in sys.stdin:
    edges = [int(x) for x in line.split("x")]

    edges.sort()
    ribbon = sum(x * 2 for x in edges[:2])

    l, w, h = edges
    bow = l * w * h

    total += bow + ribbon

print(total)
