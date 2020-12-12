#!/usr/bin/env python3

from .ship_maths import process_move

from typing import List


def part_2(instructions: List[str]):
    ship_x, ship_y = [0, 0]
    offset_x, offset_y = [10, 1]

    for instruction in instructions:
        command, value = instruction[0], int(instruction[1:])
        if command in ['N', 'S', 'E', 'W']:
            offset_x, offset_y = process_move([offset_x, offset_y], command, value)
        elif command == 'F':
            ship_x = ship_x + (value * offset_x)
            ship_y = ship_y + (value * offset_y)
        elif command == 'L':
            num_rotations = int(value / 90)
            for i in range(num_rotations):
                offset_x, offset_y = -offset_y, offset_x
        elif command == 'R':
            num_rotations = int(value / 90)
            for i in range(num_rotations):
                offset_x, offset_y = offset_y, -offset_x

    return abs(ship_x) + abs(ship_y)
