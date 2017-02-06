#!/usr/bin/env python

import sys
import itertools


class RoundTable(object):

    def __init__(self):
        self.people = set()
        self.happiness = {}

    def parse_instruction(self, instruction):
        split = instruction.split()

        person = split[0]
        neighbor = split[-1].strip('.')
        points = int(split[3])

        if (split[2] == "lose"):
            points *= -1

        self.add_relationship(person, neighbor, points)

    def add_relationship(self, person, neighbor, points):
        self.people.add(person)
        self.happiness[(person, neighbor)] = points

    def add_cool_dude(self):
        people = self.people.copy()

        for person in people:
            self.add_relationship("Kyle", person, 0)
            self.add_relationship(person, "Kyle", 0)

    def get_happiest_seating(self):
        best = None

        for seating in itertools.permutations(self.people):
            happiness = 0

            # we need to add the first person to the end of our seating chart
            # to accomodate for the circular table wrap-around
            seating = seating + (seating[0],)

            for pair in zip(seating[:-1], seating[1:]):
                rev = tuple(reversed(pair))
                happiness += self.happiness[pair]
                happiness += self.happiness[rev]

            if best is None or happiness > best["happiness"]:
                best = {"seating": seating, "happiness": happiness}

        return best


table = RoundTable()

for line in sys.stdin:
    table.parse_instruction(line)

# adds ourselves for part 2
table.add_cool_dude()
print(table.get_happiest_seating()["happiness"])
