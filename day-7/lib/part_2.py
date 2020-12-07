#!/usr/bin/env python3

from .bags import parse_restriction


def part_2(bag_restrictions):
    graph = {}

    bags_in_a_shiny_gold_bag = 0

    for restriction in bag_restrictions:
        for parent, child, weight in parse_restriction(restriction):
            if parent in graph:
                graph[parent].append((child, weight))
            else:
                graph[parent] = [(child, weight)]

    possibilities = [('shiny gold', child, weight) for (child, weight) in graph['shiny gold']]

    while possibilities:
        parent, child, weight = possibilities.pop()
        bags_in_a_shiny_gold_bag += weight
        for i in range(weight):
            if child in graph:
                possibilities += [(child, new_child, weight) for (new_child, weight) in graph[child]]

    return bags_in_a_shiny_gold_bag
