#!/usr/bin/env python3

from .ship_maths import process_move, get_compass_point_for_heading

from typing import List


def part_1(instructions: List[str]):
    heading = 90
    x, y = [0, 0]

    for instruction in instructions:
        command, value = instruction[0], int(instruction[1:])
        if command in ['N', 'S', 'E', 'W']:
            x, y = process_move([x, y], command, value)
        elif command == 'F':
            x, y = process_move([x, y], get_compass_point_for_heading(heading), value)
        elif command == 'L':
            heading -= value
            if heading <= 0:
                heading = heading % 360
        elif command == 'R':
            heading += value
            if heading >= 360:
                heading = heading % 360

    return abs(x) + abs(y)
