#!/usr/bin/env python3

day11_input = "cqjxjnds"

MIN_CHAR = ord('a')
MAX_CHAR = ord('z')
FORBIDDEN_CHARS = [ord(x) for x in ["i", "o", "l"]]

def is_forbidden_char(p, idx):
    return p[idx] in FORBIDDEN_CHARS

def has_forbidden_char(p):
    for i in range(len(p)):
        if is_forbidden_char(p, i):
            return True
    return False

def has_pairs(p):
    looking_for = None
    used_chars = []

    for i in range(0, len(p)):
        if (looking_for is None or looking_for != p[i]) and p[i] not in used_chars:
            looking_for = p[i]
        elif p[i] == looking_for:
            used_chars.append(looking_for)
            looking_for = None

    return len(used_chars) >= 2

def has_straight(p):
    last_char = p[0]
    n_straight = 1
    for i in range(1, len(p)):
        if p[i] == last_char + 1:
            n_straight += 1
            if n_straight == 3:
                return True
        else:
            # Restarting
            n_straight = 1

        last_char = p[i]

    return False

def increment(p, idx):
    p[idx] += 1
    while idx >= 0 and (p[idx] == MAX_CHAR + 1 or is_forbidden_char(p, idx)):
        if p[idx] == MAX_CHAR + 1:
            p[idx] = MIN_CHAR
            idx -= 1
            p[idx] += 1
        else:
            p[idx] += 1

def increment_first_forbidden_char(p):
    for i in range(len(p)):
        if is_forbidden_char(p, i):
            increment(p, i)
            for j in range(i + 1, len(p)):
                p[j] = MIN_CHAR
            break

def is_valid_password(p):
    return not has_forbidden_char(p) and has_pairs(p) and has_straight(p)

# TODO: What optimizations can be done?
# TODO: *

def part1():
    attempt = [ord(x) for x in day11_input]
    increment_first_forbidden_char(attempt)
    while not is_valid_password(attempt):
        increment(attempt, len(attempt) - 1)

    print("New password: {}".format("".join(chr(x) for x in attempt)))

def part2():
    prev_password = "cqjxxyzz"
    attempt = [ord(x) for x in prev_password]
    increment(attempt, len(attempt) - 1)
    increment_first_forbidden_char(attempt)
    while not is_valid_password(attempt):
        increment(attempt, len(attempt) - 1)

    print("New password: {}".format("".join(chr(x) for x in attempt)))

part1()
part2()
