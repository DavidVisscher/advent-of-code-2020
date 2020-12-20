#!/usr/bin/env python3
"""
Advent of Code 2020 day 4.
"""

from typing import List, Dict, Tuple


def read_passports(input_filename: str) -> List[Dict]:
    """
    Reads each passport from file and returns a list of parsed passports.
    """
    out = []

    with open(input_filename, "r") as passportfile:
        current_passport = ""
        for line in passportfile:
            if line.strip() != "":
                current_passport += line
            else:
                out.append(parse_passport(current_passport))
                current_passport = ""

        # Don't forget that last one!
        out.append(parse_passport(current_passport))
    return out


def parse_passport(raw_passport: str) -> Dict:
    """
    Parses a single passport.
    """
    out = {}

    for kvpair in raw_passport.split():
        key, value = kvpair.split(":")
        out[key] = value

    return out


def check_for_fields(passport: Dict, fields: List[str]) -> bool:
    """
    Checks if passport contains all fields contained in fields.
    If so, return True, else return False.
    """
    for field in fields:
        if not field in passport.keys():
            return False
    return True


def check_int_field(passport: Dict, field: str, bounds: Tuple) -> bool:
    """
    Checks if an integer field of a passport is between certain bounds.
    """
    value = int(passport[field])

    if value >= bounds[0] and value <= bounds[1]:
        return True
    return False


def check_hgt_field(passport: Dict) -> bool:
    """
    Checks if hgt is between:
        - 150 and 193 cm
        - 59 and 76 in
    """
    hgt = passport["hgt"]

    if "cm" in hgt:
        bounds = (150, 193)
    elif "in" in hgt:
        bounds = (59, 76)
    else:
        return False

    value = int(hgt.replace("cm", "").replace("in", ""))

    if value >= bounds[0] and value <= bounds[1]:
        return True
    return False


def check_hcl_field(passport: Dict) -> bool:
    """
    Checks if hcl field follows the format for a valid color.
    """
    hcl = passport["hcl"]
    
    if len(hcl) != 7:
        return False
    if hcl[0] != "#":
        return False

    valid_chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

    for char in hcl[1:]:
        if char not in valid_chars:
            return False
    return True


def check_ecl_field(passport: Dict) -> bool:
    """
    Checks if the ecl field is valid.
    """
    valid_options = ['amb','blu','brn','gry','grn','hzl','oth']

    if passport['ecl'] not in valid_options:
        return False
    return True


def check_pid_field(passport: Dict) -> bool:
    """
    Checks if hcl field follows the format for a valid color.
    """
    pid = passport["pid"]

    if len(pid) != 9:
        return False

    valid_chars = ['0','1','2','3','4','5','6','7','8','9']

    for char in pid:
        if char not in valid_chars:
            return False
    return True


def count_valid_passports(passports: List) -> int:
    """
    Checks the given passports are valid and returns
    the amount of valid passports.
    """
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    count = 0

    for passport in passports:
        if (
            check_for_fields(passport, required_fields)
            and check_int_field(passport, "byr", (1920, 2002))
            and check_int_field(passport, "iyr", (2010, 2020))
            and check_int_field(passport, "eyr", (2020, 2030))
            and check_hgt_field(passport)
            and check_hcl_field(passport)
            and check_ecl_field(passport)
            and check_pid_field(passport)
        ):
            count += 1
    return count


if __name__ == "__main__":
    passports = read_passports("input")
    print(count_valid_passports(passports))
