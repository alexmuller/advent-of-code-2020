#!/usr/bin/env python3

def part_1(input):
    joltages = sorted(input)

    jumps = {
        1: 0,
        3: 0,
    }

    previous_joltage = 0

    for i, joltage in enumerate(joltages):
        jump = joltage - previous_joltage
        jumps[jump] += 1

        previous_joltage = joltage

    return (jumps[1] * (jumps[3] + 1))
