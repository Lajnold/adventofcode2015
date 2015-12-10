#!/usr/bin/env python3

with open("day8-input.txt") as f:
    # Array of quoted strings.
    day8_input_lines = f.read().split("\n")

def part1():
    total_diff = 0

    for line in day8_input_lines:
        code_length = len(line)

        memory_length = 0

        # Check the whole string minus the surrounding quotes.
        i = 1
        while i < code_length - 1:
            memory_length += 1

            if line[i] == "\\":
                if line[i + 1] == "\\":
                    # \\
                    i += 2
                elif line[i + 1] == '"':
                    # \"
                    i += 2
                else:
                    # \x32
                    i += 4
            else:
                # Simple character.
                i += 1

        total_diff += (code_length - memory_length)

    print("Code diff: {}".format(total_diff))

def part2():
    total_diff = 0
    for line in day8_input_lines:
        code_length = len(line)

        # The surrounding quotes become "\"\"", or 6 characters.
        encoded_length = 6
        i = 1
        while i < code_length - 1:
            if line[i] == "\\":
                if line[i + 1] == "\\":
                    # \\ becomes \\\\
                    encoded_length += 4
                    i += 2
                elif line[i + 1] == '"':
                    # \" becomes \\\"
                    encoded_length += 4
                    i += 2
                else:
                    # \x32 becomes \\x32
                    encoded_length += 5
                    i += 4
            else:
                # Simple character.
                encoded_length += 1
                i += 1

        total_diff += (encoded_length - code_length)

    print("Encoded diff: {}".format(total_diff))

part1()
part2()
