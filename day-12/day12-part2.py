#!/usr/bin/env python

import json


def get_sum(node):

    if isinstance(node, int):
        return node

    if isinstance(node, dict):
        properties = node.values()

        if "red" in properties:
            return 0

        return sum([get_sum(i) for i in properties])

    if isinstance(node, list):
        return sum([get_sum(i) for i in node])

    return 0


document = json.loads(input())
print(get_sum(document))
