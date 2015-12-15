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
    used = []
    i = 0
    while i < len(p) - 1 and len(used) < 2:
        if p[i] == p[i + 1] and p[i] not in used:
            used.append(p[i])
            i += 2
        else:
            i += 1

    return len(used) >= 2

def has_straight(p):
    for i in range(0, len(p) - 2):
        if p[i] == p[i + 1] - 1 and p[i + 1] == p[i + 2] - 1:
            return True
    return False

def increment(p, idx):
    p[idx] += 1
    while p[idx] == MAX_CHAR + 1 or is_forbidden_char(p, idx):
        if p[idx] == MAX_CHAR + 1:
            # Increment prev char(s) and zero this char.
            p[idx] = MIN_CHAR
            idx -= 1
            p[idx] += 1
        else:
            # Get rid of forbidden char.
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

def part1():
    attempt = [ord(x) for x in day11_input]
    increment_first_forbidden_char(attempt)
    while not is_valid_password(attempt):
        increment(attempt, len(attempt) - 1)

    print("New password: {}".format("".join(chr(x) for x in attempt)))

def part2():
    prev_password = "cqjxxyzz"
    attempt = [ord(x) for x in prev_password]

    # Start with next increment so that the previous password isn't accepted again.
    increment(attempt, len(attempt) - 1)

    increment_first_forbidden_char(attempt)
    while not is_valid_password(attempt):
        increment(attempt, len(attempt) - 1)

    print("New password: {}".format("".join(chr(x) for x in attempt)))

part1()
part2()
