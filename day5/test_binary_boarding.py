"""
Tests for the binary boarding module.
"""

import pytest

from day5.binary_boarding import split_range, calulate_seat_id, determine_seat_from_boardingpass, \
    get_seat_id_for_boarding_pass, get_maximum_seat_id_for_boarding_passes, read_list_of_boarding_passes_from_file
from day5.exceptions import IncorrectSplitCharacterException, IncorrectBoardingPassException


def test_if_split_range_raises_on_incorrect_character_code():
    with pytest.raises(IncorrectSplitCharacterException):
        split_range("Q", (0, 127))


def test_if_row_range_splits_correctly():
    assert split_range("F", (0, 127)) == (0, 63)
    assert split_range("B", (0, 63)) == (32, 63)
    assert split_range("F", (32, 63)) == (32, 47)
    assert split_range("B", (32, 47)) == (40, 47)
    assert split_range("B", (40, 47)) == (44, 47)
    assert split_range("F", (44, 47)) == (44, 45)
    assert split_range("F", (44, 45)) == (44, 44)


def test_if_column_range_splits_correctly():
    assert split_range("R", (0, 7)) == (4, 7)
    assert split_range("L", (4, 7)) == (4, 5)
    assert split_range("R", (4, 5)) == (5, 5)


def test_seat_id_calculation():
    assert calulate_seat_id({"row": 70, "column": 7}) == 567
    assert calulate_seat_id({"row": 14, "column": 7}) == 119
    assert calulate_seat_id({"row": 102, "column": 4}) == 820


def test_wrong_boarding_pass_raises_exception():
    with pytest.raises(IncorrectBoardingPassException):
        determine_seat_from_boardingpass("QWERTY")
    with pytest.raises(IncorrectBoardingPassException):
        determine_seat_from_boardingpass("LFFFBBFRRRR")
    with pytest.raises(IncorrectBoardingPassException):
        determine_seat_from_boardingpass("LFFFBBFRR")
    with pytest.raises(IncorrectBoardingPassException):
        determine_seat_from_boardingpass("BFFFBBFFFF")
    with pytest.raises(IncorrectBoardingPassException):
        determine_seat_from_boardingpass("LFFFBBFRRR")
    with pytest.raises(IncorrectBoardingPassException):
        determine_seat_from_boardingpass("LFFFBBFFRR")


def test_seat_calculation():
    assert determine_seat_from_boardingpass("BFFFBBFRRR") == {"row": 70, "column": 7}
    assert determine_seat_from_boardingpass("FFFBBBFRRR") == {"row": 14, "column": 7}
    assert determine_seat_from_boardingpass("BBFFBBFRLL") == {"row": 102, "column": 4}


def test_seat_for_boarding_pass():
    assert get_seat_id_for_boarding_pass("BFFFBBFRRR") == 567
    assert get_seat_id_for_boarding_pass("FFFBBBFRRR") == 119
    assert get_seat_id_for_boarding_pass("BBFFBBFRLL") == 820


def test_read_passes_from_file():
    """
    Requires testpasses.txt to contain:
    BFFFBBFRRR
    FFFBBBFRRR
    BBFFBBFRLL
    """
    assert read_list_of_boarding_passes_from_file("testpasses.txt") == ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]


def test_highest_seat_id_for_boarding_passes():
    assert get_maximum_seat_id_for_boarding_passes(["BFFFBBFRRR", "FFFBBBFRRR"]) == 567
    assert get_maximum_seat_id_for_boarding_passes(["BFFFBBFRRR"]) == 567
    assert get_maximum_seat_id_for_boarding_passes(["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]) == 820
