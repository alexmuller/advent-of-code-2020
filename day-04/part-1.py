#!/usr/bin/env python

def fields_from_passport(passport):
    fields_with_data = [field for field in passport.split(" ")]
    fields = [field.split(":")[0] for field in fields_with_data]
    return fields

def process():
    filename = 'passports.txt'

    with open(filename, 'r') as f:
        data = [datum for datum in f.read().split("\n\n")]

    passports = [passport.replace("\n", " ").strip() for passport in data]

    required_fields = [
        'byr',
        'ecl',
        'eyr',
        'hcl',
        'hgt',
        'iyr',
        'pid',
    ]

    valid_passports = 0

    for passport in passports:
        fields = fields_from_passport(passport)
        if all(field in fields for field in required_fields):
            valid_passports += 1

    print("{} valid passports").format(valid_passports)

if __name__ == '__main__':
    process()
