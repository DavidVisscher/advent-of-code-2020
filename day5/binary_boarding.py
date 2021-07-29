"""
Module containing the functions for calculating the seat in binary boarding.
From advent of code day 5.
"""

from math import floor, ceil
from typing import Tuple, List

from day5.exceptions import IncorrectSplitCharacterException, IncorrectBoardingPassException


def read_list_of_boarding_passes_from_file(filename):
    out = []
    with open(filename, "r") as boarding_pass_file:
        for line in boarding_pass_file:
            out.append(line.strip())
    return out


def get_maximum_seat_id_for_boarding_passes(boarding_passes: List):
    current_max = 0

    for boarding_pass in boarding_passes:
        seat_id = get_seat_id_for_boarding_pass(boarding_pass)
        if seat_id > current_max:
            current_max = seat_id

    return current_max


def get_seat_id_for_boarding_pass(boarding_pass: str):
    seat = determine_seat_from_boardingpass(boarding_pass)
    return calulate_seat_id(seat)


def determine_seat_from_boardingpass(boarding_pass: str):
    """
    Calculates the seat from the boarding pass string.
    """
    validate_boardingpass(boarding_pass)

    row_range = (0, 127)
    column_range = (0, 7)
    out = {}

    for char in boarding_pass[:7]:
        row_range = split_range(char, row_range)
    out["row"] = row_range[0]

    for char in boarding_pass[7:]:
        column_range = split_range(char, column_range)
    out["column"] = column_range[0]

    return out


def validate_boardingpass(boarding_pass: str):
    if len(boarding_pass) != 10:
        raise IncorrectBoardingPassException(f"Length of boarding pass is incorrect: {len(boarding_pass)}")

    for index, char in enumerate(boarding_pass[:7]):
        if not char == "B" and not char == "F":
            raise IncorrectBoardingPassException(f"Incorrect character in boarding pass at position {index}")

    for index, char in enumerate(boarding_pass[7:]):
        if not char == "R" and not char == "L":
            raise IncorrectBoardingPassException(f"Incorrect character in boarding pass at position {index + 7}")


def calulate_seat_id(seat):
    return (seat["row"] * 8) + seat["column"]


def split_range(character_code: str, current_seat_range: Tuple):
    """
    Splits a range of seats based on a character code.
    F splits and keeps the upper half, L has the same functionality
    B splits and keeps the lower half, R has the same functionality.
    """
    lowest_row = current_seat_range[0]
    highest_row = current_seat_range[1]
    row_difference = highest_row - lowest_row

    if character_code == "F" or character_code == "L":
        new_highest_row = floor(highest_row - row_difference / 2)
        return (lowest_row, new_highest_row)

    elif character_code == "B" or character_code == "R":
        new_lowest_row = lowest_row + ceil(row_difference / 2)
        return (new_lowest_row, highest_row)

    else:
        raise IncorrectSplitCharacterException(f"Invalid row split character was passed : {character_code}")


if __name__ == "__main__":
    passes = read_list_of_boarding_passes_from_file("boarding_passes.txt")
    print(get_maximum_seat_id_for_boarding_passes(passes))
