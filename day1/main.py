#!/usr/bin/env python3
"""
Advent of code 2020 day 1.
"""

from typing import List
from functools import reduce
from operator import mul


def read_input(filename) -> List[int]:
    """
    Reads the inputfile and returns a sorted list of integers.
    """
    out = []

    with open(filename, 'r') as inputfile:
        for line in inputfile:
            out.append(int(line))

    return out


def find_pair(numbers: List[int], target: int) -> List[int]:
    """
    Finds a pair of numbers that sum to the target number.
    Try to do so semi-efficiently by eliminating impossible pairs.
    """
    sorted_numbers = sorted(numbers)

    for first in sorted_numbers:
        for second in reversed(sorted_numbers):
            if first + second == target:
                return [first, second]
            elif first + second < target:
                break
    
    raise Exception(f"No pair found for target: {target}")


def find_trio(numbers: List[int], target: [int]) -> List[int]:
    """
    Finds thee numbers that sum to the target.
    """
    sorted_numbers = sorted(numbers)

    for first in sorted_numbers: 
        for second in sorted_numbers:
            if first + second >= target:
                break
            for third in sorted_numbers:
                if first + second + third == target:
                    return [first, second, third]
    
    raise Exception(f"No trio found for target: {target}")


if __name__ == "__main__":
    numbers = read_input("input")
    
    result_pair = find_pair(numbers, 2020)
    print(f"Result pair found: {result_pair}, product: {reduce(mul, result_pair, 1)}")
    
    result_trio = find_trio(numbers, 2020)
    print(f"Result pair found: {result_trio}, product: {reduce(mul, result_trio, 1)}")
