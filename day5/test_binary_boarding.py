"""
Tests for the binary boarding module.
"""
import tempfile

import pytest

from day5.BoardingPass import *
from day5.binary_boarding import *
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
    assert BoardingPass(70, 7).seat_id == 567
    assert BoardingPass(14, 7).seat_id == 119
    assert BoardingPass(102, 4).seat_id == 820


def test_wrong_boarding_pass_raises_exception():
    with pytest.raises(IncorrectBoardingPassException):
        determine_seat_location_from_code("QWERTY")
    with pytest.raises(IncorrectBoardingPassException):
        determine_seat_location_from_code("LFFFBBFRRRR")
    with pytest.raises(IncorrectBoardingPassException):
        determine_seat_location_from_code("LFFFBBFRR")
    with pytest.raises(IncorrectBoardingPassException):
        determine_seat_location_from_code("BFFFBBFFFF")
    with pytest.raises(IncorrectBoardingPassException):
        determine_seat_location_from_code("LFFFBBFRRR")
    with pytest.raises(IncorrectBoardingPassException):
        determine_seat_location_from_code("LFFFBBFFRR")


def test_seat_calculation():
    assert determine_seat_location_from_code("BFFFBBFRRR") == {"row": 70, "column": 7}
    assert determine_seat_location_from_code("FFFBBBFRRR") == {"row": 14, "column": 7}
    assert determine_seat_location_from_code("BBFFBBFRLL") == {"row": 102, "column": 4}


def test_seat_for_boarding_pass():
    assert BoardingPass.from_character_code("BFFFBBFRRR").seat_id == 567
    assert BoardingPass.from_character_code("FFFBBBFRRR").seat_id == 119
    assert BoardingPass.from_character_code("BBFFBBFRLL").seat_id == 820


def test_read_pass_codes_from_file():
    testfile_handle = tempfile.mkstemp(text=True)
    with open(testfile_handle[1], 'w') as testfile:
        testfile.write("BFFFBBFRRR\nFFFBBBFRRR\nBBFFBBFRLL")

    assert read_list_of_boarding_passes_from_file(testfile_handle[1]) == ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]


def test_read_passes_from_file_and_create():
    testfile_handle = tempfile.mkstemp(text=True)
    with open(testfile_handle[1], 'w') as testfile:
        testfile.write("BFFFBBFRRR\nFFFBBBFRRR\nBBFFBBFRLL")

    boarding_passes = create_boarding_passes_from_file(testfile_handle[1])

    assert boarding_passes[0] == BoardingPass(70,7)
    assert boarding_passes[1] == BoardingPass(14,7)
    assert boarding_passes[2] == BoardingPass(102,4)


def test_highest_seat_id_for_boarding_passes():
    pass1 = BoardingPass.from_character_code("BFFFBBFRRR")
    pass2 = BoardingPass.from_character_code("FFFBBBFRRR")
    pass3 = BoardingPass.from_character_code("BBFFBBFRLL")
    assert get_maximum_seat_id_for_boarding_passes([pass1, pass2]) == 567
    assert get_maximum_seat_id_for_boarding_passes([pass2, pass1]) == 567
    assert get_maximum_seat_id_for_boarding_passes([pass1]) == 567
    assert get_maximum_seat_id_for_boarding_passes([pass1, pass2, pass3]) == 820
    assert get_maximum_seat_id_for_boarding_passes([pass1, pass3, pass2]) == 820
    assert get_maximum_seat_id_for_boarding_passes([pass3, pass2, pass1]) == 820


def test_correct_outcome_for_challenge_set():
    boarding_passes = create_boarding_passes_from_file("boarding_passes.txt")
    assert get_maximum_seat_id_for_boarding_passes(boarding_passes) == 866
    assert find_gaps_between_boarding_passes(boarding_passes) == [583]


def test_boarding_passes_eq():
    pass1 = BoardingPass(1, 1)
    pass2 = BoardingPass(1, 1)
    pass3 = BoardingPass(1, 2)
    assert pass1 == pass2
    assert not pass1 == pass3
    assert pass1 != pass3
    assert not pass2 == pass3
    assert pass2 != pass3


def test_boarding_passes_lt_gt():
    pass1 = BoardingPass(1, 3)
    pass2 = BoardingPass(2, 1)
    pass3 = BoardingPass(3, 1)
    assert pass1 < pass2
    assert pass2 > pass1
    assert pass1 < pass2 < pass3
    assert pass3 > pass2 > pass1


def test_sorting_boarding_passes():
    pass1 = BoardingPass(3, 1)
    pass2 = BoardingPass(50, 1)
    pass3 = BoardingPass(50, 2)
    passes = [pass3, pass2, pass1]

    sorted_passes = sorted(passes)
    assert sorted_passes[0] == pass1
    assert sorted_passes[1] == pass2
    assert sorted_passes[2] == pass3


def test_find_gaps_between_boarding_passes():
    boarding_passes = [
        BoardingPass(1,1),
        BoardingPass(1,2),
        BoardingPass(1,4),
        BoardingPass(1,5),
        BoardingPass(1,6),
        BoardingPass(1,7),
        BoardingPass(1,8),
        BoardingPass(2,2)
    ]

    assert find_gaps_between_boarding_passes(boarding_passes) == [11, 17]

    boarding_passes_2 = [
        BoardingPass(1, 1),
        BoardingPass(1, 2),
        BoardingPass(1, 3),
        BoardingPass(1, 5),
        BoardingPass(1, 6),
        BoardingPass(1, 7),
        BoardingPass(1, 8),
        BoardingPass(2, 2)
    ]

    assert find_gaps_between_boarding_passes(boarding_passes_2) == [12, 17]