#!/usr/bin/env python3

with open("day17-input.txt") as f:
    day17_input_lines = f.read().split("\n")


def parse_containers(lines):
    return map(int, lines)


def part1():
    LITERS = 150

    def count_combinations(containers, taken, sum_so_far):
        num_combinations = 0
        for i in range(taken + 1, len(containers)):
            new_sum = sum_so_far + containers[i]
            if new_sum == LITERS:
                num_combinations += 1
            elif new_sum < LITERS:
                num_combinations += count_combinations(containers, i, new_sum)
        return num_combinations

    containers = sorted(parse_containers(day17_input_lines), reverse=True)
    num_combinations = count_combinations(containers, -1, 0)

    print("Combinations: {}".format(num_combinations))


def part2():
    LITERS = 150

    def count_combinations(containers, num_taken, idx_taken, sum_so_far, num_combinations):
        for i in range(idx_taken + 1, len(containers)):
            new_sum = sum_so_far + containers[i]
            new_num_taken = num_taken + 1
            if new_sum == LITERS:
                num_combinations[new_num_taken] = num_combinations.get(new_num_taken, 0) + 1
            elif new_sum < LITERS:
                count_combinations(containers, new_num_taken, i, new_sum, num_combinations)

    containers = sorted(parse_containers(day17_input_lines), reverse=True)

    num_combinations = {}
    count_combinations(containers, 0, -1, 0, num_combinations)

    min_number = sorted(num_combinations.keys())[0]

    print("Combinations with {} containers: {}".format(
          min_number,
          num_combinations[min_number]))


part1()
part2()
