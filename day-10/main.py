#!/usr/bin/env python3

from lib.part_1 import part_1
from lib.part_2 import part_2

from sys import argv


def process():
    filename = argv[1]

    with open(filename, 'r') as f:
        joltages = [int(datum.strip()) for datum in f.readlines()]

    print('Part 1: {}'.format(part_1(joltages)))
    print('Part 2: {}'.format(part_2(joltages)))


if __name__ == '__main__':
    process()
