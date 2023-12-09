import re
import os
import time
from timeit import timeit

import sys

sys.path.append(os.path.abspath(os.path.curdir))
from utils.common_functions import grab_all_lines_from_file
from utils.pretty_print import pprint

example1 = grab_all_lines_from_file("day1/example1.txt")
example2 = grab_all_lines_from_file("day1/example2.txt")
input = grab_all_lines_from_file("day1/input.txt")

numbers: list[str] = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

number_dict: dict[str, str] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def sum_calibration_values(lines, method):
    return sum(method(line) for line in lines)


def day_1_part_1():
    # Challenge: What is the sum of all calibration values?
    # Calibration value is combinging the first and last digit from each line
    # and adding them together
    # Example: 1234 -> 1 + 4 = 5

    regex = re.compile(r"[^\d]*(\d?).*(\d)")

    def get_calibration_value(line: str) -> int:
        numbers_in_line = [char for char in line if char.isdigit()]
        return int(numbers_in_line[0] + numbers_in_line[-1])

    def get_calibration_value_regex(line) -> int:
        first, last = regex.search(line).groups()
        return int((first or last) + last)

    return [
        "Challenge 1",
        sum_calibration_values(example1, get_calibration_value),
        sum_calibration_values(input, get_calibration_value),
        timeit(lambda: sum_calibration_values(input, get_calibration_value), number=1000),
    ]


# Complexity: O(n*(n+n^2+nlogn)) -> O(n^3)
def day_1_part_2():
    # Challenge: What is the sum of all calibration values?
    # Calibration value is combinging the first and last number from each line
    # and adding them together
    # Example: 123four -> 1 + four = 5

    # Complexity: O(n+n^2+nlogn))
    def get_calibration_value(line: str) -> int:
        numbers_in_line = {i: c for i, c in enumerate(line) if c.isdigit()}

        for number in numbers:
            index = 0
            while index < len(line):
                index_of_number = line.find(number, index)

                if index_of_number == -1:
                    break

                index = index_of_number + len(number) + 1
                numbers_in_line[index_of_number] = number_dict[number]

        first_number_key = (sorted_list := list(sorted(numbers_in_line.keys())))[0]
        last_number_key = sorted_list[-1]
        calibration_value = numbers_in_line[first_number_key] + numbers_in_line[last_number_key]

        return int(calibration_value)

    return [
        "Challenge 2",
        sum_calibration_values(example2, get_calibration_value),
        sum_calibration_values(input, get_calibration_value),
        timeit(lambda: sum_calibration_values(input, get_calibration_value), number=1000),
    ]


pprint("Day 1", [day_1_part_1(), day_1_part_2()])
