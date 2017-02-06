#!/usr/bin/env python


class SantasMap():
    def __init__(self):
        self.position = (0, 0)
        self.visited = {}

    def move(self, direction):
        if direction == "^":
            self.add_pos((0, 1))
        elif direction == "v":
            self.add_pos((0, -1))
        elif direction == ">":
            self.add_pos((1, 0))
        elif direction == "<":
            self.add_pos((-1, 0))
        self.visited[self.position] = True

    def add_pos(self, pos):
        cur_x, cur_y = self.position
        add_x, add_y = pos
        self.position = (cur_x + add_x, cur_y + add_y)

    def get_unique_visits(self):
        return len(self.visited)

santas_map = SantasMap()
with open("./input") as f:
    while True:

        direction = f.read(1)
        if not direction:
            break

        santas_map.move(direction)

print(santas_map.get_unique_visits())
