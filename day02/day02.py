import sys
import numpy as np
import math

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2017\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day02/"


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [
        [int(x) for x in line.rstrip().replace("	", " ").split(" ")] for line in content
    ]
    # return [line.rstrip().replace("	", " ").split(" ") for line in content]


# Part 1
def part1_solve(input):
    sum = 0

    for row in input:
        row.sort()

        for index, value in enumerate(row):
            found_pair = False
            for x in range(index + 1, len(row)):
                if row[x] % value == 0:
                    sum += row[x] // value
                    found_pair = True
                    break

            if found_pair:
                break

    return sum


# Part 2
def part2_solve(input):
    pass


if __name__ == "__main__":
    test_input = get_input(PATH + "test_input")
    # print(test_input)

    print(part1_solve(test_input))

    real_input = get_input(PATH + "real_input")
    # print(real_input)
    print(part1_solve(real_input))
