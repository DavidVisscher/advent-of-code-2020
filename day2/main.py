#!/usr/bin/env python3
"""
Advent of code 2020 day 2.
"""

from typing import List, Dict


def read_passwords(filename: str) -> List[Dict]:
    """
    Reads passwords from the inputfile, and returns them as a list.
    """
    out = []
    with open(filename, 'r') as passwordfile:
        for line in passwordfile:
            out.append(parse_password(line))
    return out


def parse_password(raw_password: str) -> Dict:
    """
    Takes a raw inputline and outputs each password as a dict of 
    the following format:
        {"min": int, "max": int, "constrained_char": str, "password": str }
    from a line of the following format:
        [min]-[max] [constrained_char]: [password]
    """
    out = {}

    bounds, raw_char, password = raw_password.split(" ")
    minimum, maximum = bounds.split("-") 

    out["constrained_char"] = raw_char[0]
    out["password"] = password.strip()
    out["min"] = int(minimum)
    out["max"] = int(maximum)

    return out


def is_valid_pt1(password):
    """
    Checks if a single password is valid.

    Part 1 of challenge.
    Password must contain a constrained char a between a minimum and maximum 
    amount of times.
    """
    charcount = 0
    for char in password['password']:
        if char == password['constrained_char']:
            charcount += 1

    if charcount >= password['min'] and charcount <= password['max']:
        return True
    return False


def is_valid_pt2(password):
    """
    Checks if a single password is valid.

    Part 2 of challenge.
    Password must contain the constrained char in one of two positions, 
    but not in both.

    Indices are off-by-one on this one, so str[0] is index 1.
    """
    validity = False
    
    # unpack some values for legibility
    constrained_char = password['constrained_char']
    password_text = password['password']
    minimum = password['min']
    maximum = password['max']

    if password_text[minimum-1] == constrained_char:
        validity = not validity
    if password_text[maximum-1] == constrained_char:
        validity = not validity
    
    return validity


if __name__ == "__main__":
    passwords = read_passwords("input")

    # Part 1
    validities = map(is_valid_pt1, passwords)
    validity_count = sum([bool(x) for x in validities])
    print(validity_count)

    # Part 2
    validities = map(is_valid_pt2, passwords)
    validity_count = sum([bool(x) for x in validities])
    print(validity_count)
