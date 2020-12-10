#!/usr/bin/env python3

def calculate_paths_from(initial_joltage, paths, joltages):
    if initial_joltage in paths:
        return paths[initial_joltage]

    paths[initial_joltage] = 0

    for i in range(1, 4):
        target_joltage = initial_joltage + i
        if target_joltage in joltages:
            paths[initial_joltage] += calculate_paths_from(target_joltage, paths, joltages)

    return paths[initial_joltage]


def part_2(input):
    joltages = sorted(input)
    target_joltage = joltages[-1]

    paths = {
        target_joltage: 1
    }

    calculate_paths_from(0, paths, joltages)

    return paths[0]
