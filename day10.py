#!/usr/bin/env python3

day10_input = "1321131112"

def apply_look_and_say(input_string, n_times):
    cur_string = input_string

    for i in range(n_times):
        cur_result = ""
        cur_char = cur_string[0]
        cur_run = 1
        for i in range(1, len(cur_string)):
            if cur_char != cur_string[i]:
                cur_result += str(cur_run) + cur_char
                cur_char = cur_string[i]
                cur_run = 1
            else:
                cur_run += 1

        cur_result += str(cur_run) + cur_char

        cur_string = cur_result

    return cur_string

def part1():
    result = apply_look_and_say(day10_input, 40)
    print("Length of result: {}".format(len(result)))

def part2():
    result = apply_look_and_say(day10_input, 50)
    print("Length of result: {}".format(len(result)))

part1()
part2()
