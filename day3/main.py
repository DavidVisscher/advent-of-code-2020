#!/usr/bin/env python3
"""
Advent of Code 2020 day 3.
"""

from typing import List


def read_landscape(landscape_filename: str) -> List[List[str]]:
    """
    Reads landscape from an inputfile and returns it as a 2d array.
    """
    out = []
    with open(landscape_filename, 'r') as landscapefile:
        for line in landscapefile:
            out.append([])
            for char in line.strip():
                out[-1].append(char)
    return out


def sled_down(landscape: List[List[str]], start: tuple, move_speed: tuple) -> int:
    """
    Sled down the landscape.

    Start point is defined a tuple of (x, y).

    Movement speed is defined by a tuple of (x,y).
    Sled will move this amount each tick.

    Function will return the amount of trees encountered.
    """
    tree_count = 0

    # unpack some values
    current_x, current_y = start
    move_x, move_y = move_speed 

    while current_y < len(landscape):
        if landscape[current_y][current_x] == '#':
            tree_count += 1

        current_x += move_x
        current_x = current_x % len(landscape[0])

        current_y += move_y

    return tree_count

if __name__ == "__main__":
    landscape = read_landscape("input")
    r1d1 = sled_down(landscape, (0,0), (1,1))
    r3d1 = sled_down(landscape, (0,0), (3,1))
    r5d1 = sled_down(landscape, (0,0), (5,1))
    r7d1 = sled_down(landscape, (0,0), (7,1))
    r1d2 = sled_down(landscape, (0,0), (1,2))

    print(r1d1 * r3d1 * r5d1 * r7d1 * r1d2)
