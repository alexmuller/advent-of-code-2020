#!/usr/bin/env python3

from .computer import Computer


def part_1(instructions):
    c = Computer(instructions)

    try:
        return c.execute()
    except BaseException, err:
        return '{}'.format(err)
