#!/usr/bin/env python

def password_is_valid(first_index, second_index, required_character, password):
    results = []

    for index in [first_index, second_index]:
        results.append(password[index-1] == required_character)

    if results == [True, False] or results == [False, True]:
        return True
    else:
        return False

def process():
    results = []
    filename = 'input.txt'

    with open(filename, 'r') as f:
        data = [datum for datum in f.readlines()]

    for datum in data:
        indices, character, password = datum.split(' ')
        first_index, second_index = indices.split('-')
        character = character[0]
        results.append(password_is_valid(int(first_index), int(second_index), character, password))

    print(len([x for x in results if x == True]))

if __name__ == '__main__':
    process()
