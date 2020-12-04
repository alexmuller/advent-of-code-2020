#!/usr/bin/env python

import re

def validate_byr(byr):
    return 1920 <= int(byr) <= 2002

def validate_iyr(iyr):
    return 2010 <= int(iyr) <= 2020

def validate_eyr(eyr):
    return 2020 <= int(eyr) <= 2030

def validate_hgt(hgt):
    unit = hgt[-2:]
    if unit == 'cm':
        return 150 <= int(hgt[:-2]) <= 193
    elif unit == 'in':
        return 59 <= int(hgt[:-2]) <= 76
    else:
        return False

def validate_hcl(hcl):
    return re.search(r'^#([a-f0-9]){6}$', hcl)

def validate_ecl(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def validate_pid(pid):
    return re.search(r'^([0-9]){9}$', pid)

def validate_cid(cid):
    return True

def data_from_passport(passport):
    fields_with_data = [field for field in passport.split(" ")]
    fields = [field.split(":") for field in fields_with_data]
    return dict(fields)

FIELD_VALIDATION = {
    'byr': validate_byr,
    'iyr': validate_iyr,
    'eyr': validate_eyr,
    'hgt': validate_hgt,
    'hcl': validate_hcl,
    'ecl': validate_ecl,
    'pid': validate_pid,
    'cid': validate_cid,
}

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
        data = data_from_passport(passport)

        if not all(field in data.keys() for field in required_fields):
            continue

        validation_results = [FIELD_VALIDATION[field_name](field_value) for field_name, field_value in data.items()]

        if len(validation_results) > 0 and all(validation_results):
            valid_passports += 1

    print("{} valid passports").format(valid_passports)

if __name__ == '__main__':
    process()
