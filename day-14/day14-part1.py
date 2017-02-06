#!/usr/bin/env python

import sys
import itertools


class Reindeer(object):

    def __init__(self, name, speed, active_time, rest_time):
        self.name = name
        self.speed = speed
        self.active_time = active_time
        self.rest_time = rest_time

    def get_distance_after(self, seconds):
        single_cycle = [self.speed] * self.active_time + [0] * self.rest_time
        cycle = itertools.cycle(single_cycle)
        distance = 0
        for _ in range(seconds):
            distance += next(cycle)

        return distance


class Race(object):

    def __init__(self):
        self.racers = []
        self.results = {}

    def add_reindeer(self, desc):
        # [0|name] can fly [3|speed] km/s for [6|active_time] seconds, but then
        # must rest for [13|rest_time] seconds.
        s = desc.split()
        reindeer = Reindeer(s[0], int(s[3]), int(s[6]), int(s[13]))
        self.racers.append(reindeer)

    def get_fastest_over(self, seconds):
        fastest = None
        for reindeer in self.racers:
            distance = reindeer.get_distance_after(seconds)
            self.results[reindeer.name] = distance
            if fastest is None or fastest["distance"] < distance:
                fastest = {"reindeer": reindeer.name, "distance": distance}

        return fastest


race = Race()

for line in sys.stdin:
    race.add_reindeer(line)

print(race.get_fastest_over(2503))
print(race.results)
