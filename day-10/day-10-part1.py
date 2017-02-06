#!/usr/bin/env python

import re


def look_say_sequence(number):
    matches = re.finditer(r"(\d)\1*", number)
    groups = [m.group() for m in matches if m]

    number = ""

    for group in groups:
        segment = str(len(group)) + group[0]
        number += segment

    return number

number = input()

for _ in range(50):
    number = look_say_sequence(number)

print(len(number))
