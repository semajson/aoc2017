import sys
import numpy as np
import math

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2017\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day01/"


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content][0]


# Part 1
def part1_solve(number):
    print(number)
    sum = 0
    for index, digit in enumerate(number):
        if index == (len(number) - 1):
            # List wraps around
            next_digit = int(number[0])
        else:
            next_digit = int(number[index + 1])

        if int(digit) == next_digit:
            sum += int(digit)

    return sum


# Part 2
def part2_solve(number):
    sum = 0
    for index, digit in enumerate(number):
        # Now, the digit we check against is half away around the number list
        next_index = int((index + len(number) / 2) % (len(number)))
        next_digit = int(number[next_index])

        if int(digit) == next_digit:
            sum += int(digit)

    return sum


if __name__ == "__main__":

    # test_input = get_input(PATH + "test_input")
    # print(part1_solve(test_input))

    # real_input = get_input(PATH + "real_input")
    # print(part1_solve(real_input))

    test_input = get_input(PATH + "test_input")
    print(part2_solve(test_input))

    real_input = get_input(PATH + "real_input")
    print(part2_solve(real_input))
