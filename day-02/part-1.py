#!/usr/bin/env python

def password_is_valid(lower_bound, upper_bound, required_character, password):
    result = password.count(required_character)
    return lower_bound <= result <= upper_bound

def process():
    results = []
    filename = 'input.txt'

    with open(filename, 'r') as f:
        data = [datum for datum in f.readlines()]

    for datum in data:
        bounds, character, password = datum.split(' ')
        lower_bound, upper_bound = bounds.split('-')
        character = character[0]
        results.append(password_is_valid(int(lower_bound), int(upper_bound), character, password))

    print(len([x for x in results if x == True]))

if __name__ == '__main__':
    process()
