import sys
import numpy as np
import math

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2017\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day03/"

# calc coord of the passed in number relative to the centre
# For this function, the coord of the center of array is 0,0
def convert_num_to_coord(number):
    # For this layer of the square, calculate the largest number contained in the layer.
    # This will be the bottom left the memory grid matrix, and it will
    # be the square of an odd number.
    # Can use this number as a reference point to find the coord of the passed in number
    side_length = math.ceil(math.sqrt(number))
    if side_length % 2 == 0:
        side_length += 1

    bot_left_index = [side_length // 2, -(side_length // 2)]

    # Starting from bottom left (the square of the side length)
    # calculate how far in the left, right, up, down directions
    # we need to get to the passed in number
    x = side_length ** 2 - number

    move_left = 0
    move_up = 0
    move_right = 0
    move_down = 0

    if x < ((side_length - 1) * 1):
        move_left = x

    elif x < ((side_length - 1) * 2):
        move_left = side_length - 1
        move_up = x - (side_length - 1)

    elif x < ((side_length - 1) * 3):
        move_left = side_length - 1
        move_up = side_length - 1
        move_right = x - (side_length - 1) * 2

    elif x < ((side_length - 1) * 4):
        move_left = side_length - 1
        move_up = side_length - 1
        move_right = side_length - 1
        move_down = x - (side_length - 1) * 3

    index = bot_left_index
    index[0] += move_right - move_left
    index[1] += move_up - move_down
    return index


def build_memory_grid(number):
    # First, need to find the size of the matrix to make
    side_length = math.ceil(math.sqrt(number))
    if side_length % 2 == 0:
        side_length += 1

    # Create empty grid
    grid = np.zeros((side_length, side_length))
    grid = grid.astype(int)

    # Fill in the matrix by mapping numbers to their matrix
    # indexes
    # Note, the numbers don't start at 1 here
    num = 1
    while num <= (side_length ** 2):
        x, y = convert_num_to_coord(num)
        i = x + (side_length // 2)
        j = y + (side_length // 2)
        grid[i][j] = num

        num += 1

    return grid


# Part 1
def part1_solve_quick(number):
    x, y = convert_num_to_coord(number)
    return abs(x) + abs(y)


# Part 2
def part2_solve(target):
    # Don't need to choose grid as large as target as we will
    # will likely hit the target number much sooner.
    # Note, for larger inputs 1000 might need to be increased here
    grid = build_memory_grid(1000)

    # Create the new grid
    side_length = math.ceil(math.sqrt(1000))
    if side_length % 2 == 0:
        side_length += 1
    new_grid = np.zeros((side_length, side_length))
    new_grid = new_grid.astype(int)

    # Loop through new grid, using the algo
    # new grid value = sum of surrounding values in new grid (before new value filled in)
    sum = 0
    number = 1
    while sum <= target:
        sum = 0

        # Special case for first number
        if number == 1:
            sum = 1

        x, y = convert_num_to_coord(number)
        i = x + (side_length // 2)
        j = y + (side_length // 2)

        # Sum all the neighs in new_grid for this square
        neighs = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        for neigh in neighs:
            neigh_value = new_grid[i + neigh[0]][j + neigh[1]]
            sum += neigh_value

        new_grid[i][j] = sum
        number += 1
    return sum


if __name__ == "__main__":

    test_input = 23
    print(part2_solve(test_input))

    real_input = 312051
    print(part2_solve(real_input))
