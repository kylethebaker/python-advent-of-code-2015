#!/usr/bin/env python

import sys
import re


class LightGrid(object):

    def __init__(self):
        self.grid = [[0 for x in range(1000)] for y in range(1000)]
        self.input_re = re.compile(r""
                                   r"^(?P<action>turn on|turn off|toggle) "
                                   r"(?P<start>\d*,\d*) "
                                   r"through "
                                   r"(?P<end>\d*,\d*)$")

    def follow_instruction(self, instruction):
        action, start, stop = self.__parse_instruction(instruction)
        self.__toggle_lights(action, start, stop)

    def __parse_instruction(self, instruction):
        m = self.input_re.match(instruction)
        start = tuple([int(x) for x in m.group("start").split(",")])
        stop = tuple([int(x) for x in m.group("end").split(",")])
        return m.group("action"), start, stop

    def __toggle_lights(self, action, start, stop):
        start_x, start_y = start
        stop_x, stop_y = stop

        for x in range(start_x, stop_x + 1):
            for y in range(start_y, stop_y + 1):

                if action == "turn on":
                    self.grid[x][y] += 1

                elif action == "turn off":
                    if self.grid[x][y] != 0:
                        self.grid[x][y] -= 1

                elif action == "toggle":
                    self.grid[x][y] += 2

    def total_lights_on(self):
        total = 0
        for row in self.grid:
            total += sum(row)
        return total

grid = LightGrid()
for instruction in sys.stdin:
    grid.follow_instruction(instruction)
print(grid.total_lights_on())
