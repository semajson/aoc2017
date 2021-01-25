import sys

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2017\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day04/"


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


# Part 1
def part1_solve(passphrases):
    valid_passphrases = 0

    for passphrase in passphrases:
        passphrase = passphrase.split(" ")
        seen_words = set()
        is_valid = True

        # Don't allow duplicate words in the passphrase
        for word in passphrase:
            if word not in seen_words:
                seen_words.add(word)
            else:
                # This is an invalid passphrase, break
                is_valid = False
                break

        if is_valid:
            valid_passphrases += 1

    return valid_passphrases


# Part 2
def part2_solve(passphrases):
    valid_passphrases = 0

    for passphrase in passphrases:
        passphrase = passphrase.split(" ")
        seen_anagrams = set()
        is_valid = True

        # Don't allow anagrams in the passphrase
        for word in passphrase:

            # Here, we sort the word into alphabetical order.
            # This makes checking for anagrams much easier, if
            # two words are anagrams, they will be the same
            # when ordered alphabetically
            word_anagram = "".join(sorted(word))
            if word_anagram not in seen_anagrams:
                seen_anagrams.add(word_anagram)
            else:
                # This is an invalid passphrase, break
                is_valid = False
                break

        if is_valid:
            valid_passphrases += 1

    return valid_passphrases


if __name__ == "__main__":

    test_input = get_input(PATH + "test_input")
    print(part1_solve(test_input))

    real_input = get_input(PATH + "real_input")
    print(part1_solve(real_input))
