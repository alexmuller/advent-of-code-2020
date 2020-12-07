#!/usr/bin/env python3

from .bags import parse_restriction


def part_1(bag_restrictions):
    graph = {}

    places_to_put_a_shiny_gold_bag = []

    for restriction in bag_restrictions:
        for parent, child, weight in parse_restriction(restriction):
            if child in graph:
                graph[child].append((parent, weight))
            else:
                graph[child] = [(parent, weight)]

    possibilities = [colour for (colour, weight) in graph['shiny gold']]

    while possibilities:
        current = possibilities.pop()
        places_to_put_a_shiny_gold_bag.append(current)
        if current in graph:
            possibilities += [colour for (colour, weight) in graph[current]]

    return len(set(places_to_put_a_shiny_gold_bag))
