#!/usr/bin/env python

import sys
import itertools
from collections import defaultdict


class Map(object):

    def __init__(self):
        self.places = set()
        self.paths = defaultdict(list)
        self.distances = {}

    def add_path(self, start, end, distance):
        """ Add a path to the map """

        # add path starting from start
        self.places.add(start)
        self.paths[start].append(end)
        self.distances[(start, end)] = distance

        # add reverse
        self.places.add(end)
        self.paths[end].append(start)
        self.distances[(end, start)] = distance

    def get_shortest_route(self):
        """ Get the shortest route from all possible locations """

        shortest = None

        for route in itertools.permutations(self.places):
            distance = 0

            for segment in zip(route[:-1], route[1:]):
                distance += self.distances[segment]

            if shortest is None or distance < shortest["distance"]:
                shortest = {"route": route, "distance": distance}

        return shortest["distance"]

    def get_longest_route(self):
        """ Get the longest route from all possible locations """

        longest = None

        for route in itertools.permutations(self.places):
            distance = 0

            for segment in zip(route[:-1], route[1:]):
                distance += self.distances[segment]

            if longest is None or distance > longest["distance"]:
                longest = {"route": route, "distance": distance}

        return longest["distance"]


map = Map()
for line in sys.stdin:
    path = line.split()
    map.add_path(path[0], path[2], int(path[-1]))
print(map.get_shortest_route())
print(map.get_longest_route())
