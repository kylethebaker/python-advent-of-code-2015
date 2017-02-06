#!/usr/bin/env python

import re

matches = re.finditer("(-?[0-9]+)", input())
total = sum([int(m.group()) for m in matches if m])

print(total)
