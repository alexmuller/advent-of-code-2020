#!/usr/bin/env python

from math import ceil

def retrieve_coordinate(data, x_coordinate, y_coordinate):
    line = data[y_coordinate]
    long_line = line * 100

    return long_line[x_coordinate]

def process():
    results = []
    filename = 'input.txt'
    x = 0
    y = 0

    with open(filename, 'r') as f:
        data = [datum.strip() for datum in f.readlines()]

    while y < len(data)-1:
        x += 3
        y += 1
        results.append(retrieve_coordinate(data, x, y))

    print("Blanks: {}".format(results.count('.')))
    print("Trees: {}".format(results.count('#')))

if __name__ == '__main__':
    process()
