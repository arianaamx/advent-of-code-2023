import os
import re
from collections import defaultdict
from timeit import timeit

import sys

sys.path.append(os.path.abspath(os.path.curdir))
from utils.common_functions import grab_all_lines_from_file
from utils.pretty_print import pprint

example1 = grab_all_lines_from_file("day2/example1.txt")
example2 = grab_all_lines_from_file("day2/example2.txt")
input = grab_all_lines_from_file("day2/input.txt")


def get_max_value_of_cubes_per_game(line: str):
    # If element is not in dict, set element to 0
    cubes_dict = defaultdict(int)
    game_num_string, game_sets = line.split(": ")

    # Game 1 -> 1
    game_num = int(game_num_string.split(" ")[1])

    # 1 red, 1 green, 1 blue; 2 red, 1 green -> ["1 red, 1 green, 1 blue", "2 red, 1 green"]
    for game_set in game_sets.split("; "):
        # 1 red, 1 green, 1 blue -> ["1 red", "1 green", "1 blue"]
        for cube in game_set.split(", "):
            # 1 red -> ["1", "red"]
            cube_num, cube_color = cube.split(" ")

            # (red, 0) -> (red, 1)
            if cubes_dict[cube_color] < int(cube_num):
                cubes_dict[cube_color] = int(cube_num)

    return [game_num, cubes_dict]


def day2_part1():
    # Challenge: Determine which games would have been possible if the bag
    # had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.
    # What is the sum of the IDs of those games?

    def part1_solution(input) -> int:
        _sum = 0
        for line in input:
            game_num, cubes_dict = get_max_value_of_cubes_per_game(line)
            if cubes_dict["red"] <= 12 and cubes_dict["green"] <= 13 and cubes_dict["blue"] <= 14:
                _sum += game_num
        return _sum

    return [
        "Challenge 1",
        part1_solution(example1),
        part1_solution(input),
        timeit(lambda: part1_solution(input), number=1000),
    ]


def day2_part2():
    # The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
    # The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively.
    # Adding up these five powers produces the sum 2286.

    def part2_solution(input) -> int:
        _sum = 0
        for line in input:
            _, cubes_dict = get_max_value_of_cubes_per_game(line)
            multiply_cubes = cubes_dict["red"] * cubes_dict["green"] * cubes_dict["blue"]
            _sum += multiply_cubes
        return _sum

    return [
        "Challenge 2",
        part2_solution(example2),
        part2_solution(input),
        timeit(lambda: part2_solution(input), number=1000),
    ]


pprint("Day 2", [day2_part1(), day2_part2()])
