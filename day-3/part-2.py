#!/usr/bin/env python

from functools import reduce
from math import ceil

def retrieve_coordinate(data, (x, y)):
    line = data[y]
    long_line = line * 100

    return long_line[x]

def process():
    trees = []
    filename = 'input.txt'
    beginnings = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    with open(filename, 'r') as f:
        data = [datum.strip() for datum in f.readlines()]

    for (slope_x, slope_y) in beginnings:
        results = []
        x = slope_x
        y = slope_y
        while y < len(data):
            results.append(retrieve_coordinate(data, (x, y)))
            x += slope_x
            y += slope_y

        trees.append(results.count('#'))

    print(trees)
    print(reduce(lambda x, y: x*y, trees))

if __name__ == '__main__':
    process()
