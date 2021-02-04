import sys

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2017\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day05/"


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [int(line.rstrip()) for line in content]


# Part 1
def part1_solve(instructions):
    steps = 0
    index = 0
    while index < len(instructions):
        new_index = index + instructions[index]
        instructions[index] += 1
        index = new_index
        steps += 1

    return steps


# Part 2
def part2_solve(instructions):
    steps = 0
    index = 0
    while index < len(instructions):
        new_index = index + instructions[index]
        if (new_index - index) > 2:
            instructions[index] -= 1
        else:
            instructions[index] += 1
        index = new_index
        steps += 1

    return steps


if __name__ == "__main__":

    test_input = get_input(PATH + "test_input")
    print(part2_solve(test_input))

    real_input = get_input(PATH + "real_input")
    print(part2_solve(real_input))
