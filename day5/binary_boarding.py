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


def get_maximum_seat_id_for_boarding_passes(boarding_passes: List):
    current_max = 0

    for boarding_pass in boarding_passes:
        if boarding_pass.seat_id > current_max:
            current_max = boarding_pass.seat_id

    return current_max


def create_boarding_passes_from_file(filename):
    pass_codes = read_list_of_boarding_passes_from_file(filename)
    out = []

    for pass_code in pass_codes:
        out.append(BoardingPass.from_character_code(pass_code))
    return out


def find_gaps_between_boarding_passes(boarding_passes):
    seats_present = []
    out = []

    for boarding_pass in sorted(boarding_passes):
        seats_present.append(boarding_pass.seat_id)

    for i in range(seats_present[0], seats_present[-1]):
        if i not in seats_present:
            out.append(i)

    return out