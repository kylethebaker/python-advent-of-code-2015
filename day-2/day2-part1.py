#!/usr/bin/env python

import sys

total = 0
for line in sys.stdin:
    l, w, h = [int(x) for x in line.split("x")]
    sides = [l*w, l*h, w*h]
    perimeter = sum([side * 2 for side in sides])
    slack = min(sides)
    total += perimeter + slack

print(total)
