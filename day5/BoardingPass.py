from math import floor, ceil
from typing import Tuple

from day5.exceptions import IncorrectSplitCharacterException, IncorrectBoardingPassException


class BoardingPass():

    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column
        self.code = "XXXXXXXXXX"

    @property
    def seat_id(self):
        return (self.row * 8) + self.column

    def __eq__(self, other):
        return self.seat_id == other.seat_id

    def __lt__(self, other):
        return self.seat_id < other.seat_id

    @classmethod
    def validate_code(cls, boarding_pass_code):
        if len(boarding_pass_code) != 10:
            raise IncorrectBoardingPassException(f"Length of boarding pass is incorrect: {len(boarding_pass_code)}")

        for index, char in enumerate(boarding_pass_code[:7]):
            if not char == "B" and not char == "F":
                raise IncorrectBoardingPassException(f"Incorrect character in boarding pass at position {index}")

        for index, char in enumerate(boarding_pass_code[7:]):
            if not char == "R" and not char == "L":
                raise IncorrectBoardingPassException(f"Incorrect character in boarding pass at position {index + 7}")

    @classmethod
    def from_character_code(cls, boarding_pass_code: str):
        seat_location = determine_seat_location_from_code(boarding_pass_code)
        boarding_pass = cls(seat_location["row"], seat_location["column"])
        boarding_pass.code = boarding_pass_code
        return boarding_pass


def determine_seat_location_from_code(boarding_pass_code):
    """
    Calculates the seat from the boarding pass string.
    """
    BoardingPass.validate_code(boarding_pass_code)

    row_range = (0, 127)
    column_range = (0, 7)
    out = {}

    for char in boarding_pass_code[:7]:
        row_range = split_range(char, row_range)
    out["row"] = row_range[0]

    for char in boarding_pass_code[7:]:
        column_range = split_range(char, column_range)
    out["column"] = column_range[0]

    return out


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
        return lowest_row, new_highest_row

    elif character_code == "B" or character_code == "R":
        new_lowest_row = lowest_row + ceil(row_difference / 2)
        return new_lowest_row, highest_row

    else:
        raise IncorrectSplitCharacterException(f"Invalid row split character was passed : {character_code}")
