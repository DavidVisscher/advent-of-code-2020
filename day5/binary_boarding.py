"""
Module containing the functions for calculating the seat in binary boarding.
From advent of code day 5.
"""

from typing import List

from day5.BoardingPass import BoardingPass


def read_list_of_boarding_passes_from_file(filename):
    out = []
    with open(filename, "r") as boarding_pass_file:
        for line in boarding_pass_file:
            out.append(line.strip())
    return out


def get_maximum_seat_id_for_boarding_passes(boarding_pass_codes: List):
    current_max = 0

    for boarding_pass_code in boarding_pass_codes:
        boarding_pass = BoardingPass.from_character_code(boarding_pass_code)
        if boarding_pass.seat_id > current_max:
            current_max = boarding_pass.seat_id

    return current_max
