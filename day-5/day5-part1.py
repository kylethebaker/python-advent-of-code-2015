#!/usr/bin/env python

import sys

disallowed = ["ab", "cd", "pq", "xy"]
vowels = ["a", "e", "i", "o", "u"]


def is_nice(word):
    vowel_count = 0
    has_repeat = False
    has_disallowed = False

    for i in range(0, len(word)):
        if word[i] in vowels:
            vowel_count += 1

        if i + 1 >= len(word):
            break

        if word[i] == word[i + 1]:
            has_repeat = True

        if (word[i] + word[i + 1]) in disallowed:
            has_disallowed = True

    return (vowel_count >= 3) and has_repeat and not has_disallowed

nice_count = 0
for word in sys.stdin:
    if is_nice(word):
        nice_count += 1

print(nice_count)
