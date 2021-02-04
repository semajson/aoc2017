import sys

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2017\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day06/"


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [int(num) for num in content[0].split("\t")]


# For a given index, redistribute blocks to other
# banks
def redistribute_blocks(banks, redistr_index):
    blocks_to_redistr = banks[redistr_index]

    # Calc how many blocks should go to each other banks
    blocks_per_bank = blocks_to_redistr // len(banks)
    if blocks_per_bank == 0:
        blocks_per_bank = 1

    # Remove blocks from bank
    banks[redistr_index] = 0

    # Loop though and redistribute blocks while blocks last
    blocks_left = blocks_to_redistr
    index = redistr_index + 1
    while True:
        # If reach end of banks, loop to start at begining
        if index == len(banks):
            index = 0

        if blocks_left < blocks_per_bank:
            banks[index] += blocks_left
            break

        banks[index] += blocks_per_bank
        blocks_left -= blocks_per_bank
        index += 1


# Part 1
def part1_solve(banks):
    print(banks)
    seen_banks = []
    cycles = 0
    while banks not in seen_banks:
        cycles += 1
        seen_banks.append(banks.copy())

        # Find the largest element (if tie, get first) and
        # redistribute its blocks
        max_value_index = banks.index(max(banks))
        redistribute_blocks(banks, max_value_index)

    return cycles


def part2_solve(banks):
    print(banks)
    seen_banks = []
    cycles = 0
    while banks not in seen_banks:
        cycles += 1
        seen_banks.append(banks.copy())

        # Find the largest element (if tie, get first) and
        # redistribute its blocks
        max_value_index = banks.index(max(banks))
        redistribute_blocks(banks, max_value_index)

    # Last bank we found already in seen_banks
    return cycles - seen_banks.index(banks)


if __name__ == "__main__":

    test_input = get_input(PATH + "test_input")
    print(part2_solve(test_input))

    real_input = get_input(PATH + "real_input")
    print(part2_solve(real_input))
