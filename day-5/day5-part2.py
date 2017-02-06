#!/usr/bin/env python

import sys


def is_nice(word):
    has_pair = False
    has_sandwich = False

    for i in range(0, len(word) - 2):
        if word.count(word[i:i + 2]) >= 2:
            has_pair = True
        if word[i] == word[i + 2]:
            has_sandwich = True

    return has_pair and has_sandwich

nice_count = 0
for word in sys.stdin:
    if is_nice(word):
        nice_count += 1
print(nice_count)
