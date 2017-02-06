#!/usr/bin/env python

import sys
from collections import defaultdict


class Map(object):
    def __init__(self):
        self.places = set()
        self.paths = defaultdict(list)
        self.distances = {}

    def add_path(self, start, end, distance):
        self.places.add(start)
        self.places.add(end)
        self.paths[start].append(end)
        self.paths[end].append(start)
        self.distances[(start, end)] = distance

    def get_shortest_path(self):
        test = []
        print(self.distances)
        for p in self.places:
            test.append(self.__dijkstra(p))
        return test

    def __dijkstra(self, start):
        print("----------------------------")
        print("Testing For: ", start)
        # our starting location, with 0 distance traveled
        visited = {start: 0}

        # the final path we followed
        followed_path = {}

        # make a local copy of places to we can remove items
        places = self.places.copy()

        while places:
            print("have places: ", places)

            # of our remaining places, find the shortest distance traveled
            shortest = None
            print("shortest is:", shortest)
            for place in places:
                if place in visited:
                    if shortest is None or visited[place] < visited[shortest]:
                        print("found new shortest:", place)
                        shortest = place
            if shortest is None:
                break

            places.remove(shortest)
            print("removed shortest")
            current_distance = visited[shortest]
            print("current distance is:", current_distance)

            for path in self.paths[shortest]:
                print("checking paths for", shortest)
                try:
                    print("tring to get distance for", (shortest, path))
                    distance = (current_distance
                                + self.distances[(shortest, path)])
                except:
                    print("no distance for that path")
                    continue
                print("got distance!")
                if path not in visited or distance < visited[path]:
                    print("path wasn't visited or new distance is shorter")
                    visited[path] = weight
                    followed_path[path] = shortest

        return visited, followed_path

map = Map()
for line in sys.stdin:
    path = line.split()
    map.add_path(path[0], path[2], int(path[-1]))
print(map.get_shortest_path())
