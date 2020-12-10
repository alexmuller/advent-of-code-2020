#!/usr/bin/env python

def get_row_id(row_info):
    rows = range(128)

    for instruction in row_info:
        new_number_of_rows = len(rows) / 2
        if instruction == "F":
            rows = rows[:new_number_of_rows]
        elif instruction == "B":
            rows = rows[new_number_of_rows:]
        else:
            raise BaseException("Unknown instruction")

    if len(rows) != 1:
        raise BaseException("Bad number of rows")

    return rows[0]

def get_column_id(column_info):
    columns = range(8)

    for instruction in column_info:
        new_number_of_columns = len(columns) / 2
        if instruction == "L":
            columns = columns[:new_number_of_columns]
        elif instruction == "R":
            columns = columns[new_number_of_columns:]
        else:
            raise BaseException("Unknown instruction")

    if len(columns) != 1:
        raise BaseException("Bad number of columns")

    return columns[0]

def calculate_seat_id(row, column):
    return ((row * 8) + column)

def process():
    filename = 'boarding-passes.txt'

    with open(filename, 'r') as f:
        boarding_passes = [datum.strip() for datum in f.readlines()]

    seat_ids = []

    for boarding_pass in boarding_passes:
        row_info = boarding_pass[:7]
        column_info = boarding_pass[-3:]
        seat_ids.append(calculate_seat_id(get_row_id(row_info), get_column_id(column_info)))

    seat_ids.sort()

    for lower_bound in seat_ids:
        target_seat = lower_bound+1
        upper_bound = target_seat+2
        if target_seat not in seat_ids and upper_bound in seat_ids:
            print(target_seat)

if __name__ == '__main__':
    process()
