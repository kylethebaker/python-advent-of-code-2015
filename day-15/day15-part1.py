#!/usr/bin/env python

import sys
import re
from itertools import combinations_with_replacements


class Ingredient(object):
    def __init__(self, name, properties):
        self.name = name
        self.properties = {
            "capacity": properties[0],
            "durability": properties[1],
            "flavor": properties[2],
            "texture": properties[3],
            "calories": properties[4],
        }

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def total_from_tsps(self, tsps):
        print(sum([x * tsps for x in self.properties.values()]))


class Cupboard(object):

    def __init__(self):
        self.ingredients = []

    def add(self, ingredient):
        self.ingredients.append(ingredient)

    def get_best_cookie(self):
        recipes = combinations_with_replacement(self.ingredients, 100)
        highest_score = 0

        for combination in recipes:

            recipe = {
                "capacity": 0,
                "durability": 0,
                "flavor": 0,
                "texture": 0,
                "calories": 0,
            }

            for ing in recipe:

    def get_powerset(self):
        powerset = []
        for length in range(0, len(self.ingredients) + 1):
            for subset in itertools.combinations(self.ingredients, length):
                if not subset:
                    continue
                powerset.append(subset)
        return powerset


cupboard = Cupboard()
for line in sys.stdin:
    props = [int(n) for n in re.findall(r"-?\d+", line)]
    name = line.split(":")[0]
    cupboard.add(Ingredient(name, props))

#print([x.properties for x in cupboard.ingredients])
cupboard.get_best_cookie()
