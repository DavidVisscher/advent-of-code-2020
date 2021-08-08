"""
Contains functions to handle the I/O for the challenge.
"""
from typing import List

from day6 import CustomsGroup


def sum_unique_yes_answers_for_multiple_groups(groups: List[CustomsGroup]):
    sum_of_all_unique_yes_answers = 0
    for group in groups:
        sum_of_all_unique_yes_answers += group.unique_yes_count
    return sum_of_all_unique_yes_answers

def count_unique_yes_answers_in_file(filename: str):
    with open(filename) as inputfile:
        encoded_form_groups = inputfile.read()
    all_groups = CustomsGroup.multiple_from_str(encoded_form_groups)
    return sum_unique_yes_answers_for_multiple_groups(all_groups)

def sum_common_yes_answers_for_multiple_groups(groups: List[CustomsGroup]):
    sum_of_all_common_yes_answers = 0
    for group in groups:
        sum_of_all_common_yes_answers += group.common_yes_count
    return sum_of_all_common_yes_answers

def count_common_yes_answers_in_file(filename: str):
    with open(filename) as inputfile:
        encoded_form_groups = inputfile.read()
    all_groups = CustomsGroup.multiple_from_str(encoded_form_groups)
    return sum_common_yes_answers_for_multiple_groups(all_groups)