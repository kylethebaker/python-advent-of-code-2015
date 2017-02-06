#!/usr/bin/env python

import sys
import itertools
from operator import attrgetter


class Reindeer(object):

    def __init__(self, name, speed, active_time, rest_time):
        self.name = name
        self.speed = speed
        self.active_time = active_time
        self.rest_time = rest_time
        self.points = 0
        self.distance = 0
        self.seconds_passed = 0
        single_cycle = [self.speed] * self.active_time + [0] * self.rest_time
        self.cycle = itertools.cycle(single_cycle)

    def do_tick(self):
        self.distance += next(self.cycle)
        self.seconds_passed += 1

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

    def get_highest_score(self, seconds):
        for _ in range(seconds):
            for reindeer in self.racers:
                reindeer.do_tick()
            winning = max(self.racers, key=attrgetter("distance"))
            winning.points += 1
        return max(self.racers, key=attrgetter("points"))


race = Race()

for line in sys.stdin:
    race.add_reindeer(line)

print(race.get_highest_score(2503).points)
