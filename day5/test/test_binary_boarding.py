"""
Tests for the binary boarding module.
"""

from day5.main import *


def test_read_pass_codes_from_file():
    """
    Requires testpasses.txt to contain:
    BFFFBBFRRR
    FFFBBBFRRR
    BBFFBBFRLL
    """
    assert read_list_of_boarding_passes_from_file("day5/testpasses.txt") == ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]


def test_read_passes_from_file_and_create():
    """
    Requires testpasses.txt to contain:
    BFFFBBFRRR
    FFFBBBFRRR
    BBFFBBFRLL
    """
    boarding_passes = create_boarding_passes_from_file("day5/testpasses.txt")

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
    boarding_passes = create_boarding_passes_from_file("day5/boarding_passes.txt")
    assert get_maximum_seat_id_for_boarding_passes(boarding_passes) == 866
    assert find_gaps_between_boarding_passes(boarding_passes) == [583]


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