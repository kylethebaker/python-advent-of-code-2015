#!/usr/bin/env python


class SantasMap():
    def __init__(self):
        self.santa_position = (0, 0)
        self.dog_position = (0, 0)
        self.visited = {}
        self.is_santa = True

    def move(self, direction):
        if direction == "^":
            self.add_pos((0, 1))
        elif direction == "v":
            self.add_pos((0, -1))
        elif direction == ">":
            self.add_pos((1, 0))
        elif direction == "<":
            self.add_pos((-1, 0))

    def add_pos(self, position):
        if self.is_santa:
            cur_x, cur_y = self.santa_position
        else:
            cur_x, cur_y = self.dog_position

        add_x, add_y = position
        new_pos = (cur_x + add_x, cur_y + add_y)

        if self.is_santa:
            self.santa_position = new_pos
        else:
            self.dog_position = new_pos

        self.visited[new_pos] = True
        self.is_santa = not self.is_santa

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
