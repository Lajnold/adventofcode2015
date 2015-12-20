#!/usr/bin/env python3

with open("day15-input.txt") as f:
    day15_input = f.read()
    day15_input_lines = day15_input.split("\n")


def parse_ingredient(line):
    # Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
    split = line.replace(":", "").replace(",", "").split(" ")
    ingredient, cap, dur, fla, tex, cal = split[0], int(split[2]), int(split[4]), int(split[6]), int(split[8]), int(split[10])
    return (ingredient, cap, dur, fla, tex, cal)

def parse_ingredients(lines):
    return [parse_ingredient(line) for line in lines]

def calculate_score(amounts, ingredients):
    cap = sum(ingredients[i][1] * amounts[i] for i in range(len(amounts)))
    dur = sum(ingredients[i][2] * amounts[i] for i in range(len(amounts)))
    fla = sum(ingredients[i][3] * amounts[i] for i in range(len(amounts)))
    tex = sum(ingredients[i][4] * amounts[i] for i in range(len(amounts)))
    if cap >= 0 and dur >= 0 and fla >= 0 and tex >= 0:
        return cap * dur * fla * tex
    else:
        return 0

def calculate_calories(amounts, ingredients):
    return sum(ingredients[i][5] * amounts[i] for i in range(len(amounts)))

def part1():
    TEASPOONS = 100

    ingredients = parse_ingredients(day15_input_lines)
    amounts = [0] * len(ingredients)
    amounts[0] = TEASPOONS
    best_score = -1

    while True:
        new_score = calculate_score(amounts, ingredients)
        if new_score > best_score:
            best_score = new_score

        if amounts[-1] == TEASPOONS:
            break

        # Find rightmost index that has something to the left.
        for i in range(1, len(amounts)):
            if amounts[i - 1] != 0:
                inc = i

        # Take one from the left, and gather everything from the right.
        amounts[inc] += 1
        amounts[inc - 1] -= 1
        for i in range(inc + 1, len(amounts)):
            amounts[inc] += amounts[i]
            amounts[i] = 0

    print("Best score: {}".format(best_score))

def part2():
    TEASPOONS = 100
    CALORIES = 500

    ingredients = parse_ingredients(day15_input_lines)
    amounts = [0] * len(ingredients)
    amounts[0] = TEASPOONS
    best_score = -1

    while True:
        new_score = calculate_score(amounts, ingredients)
        new_calories = calculate_calories(amounts, ingredients)
        if new_calories == CALORIES and new_score > best_score:
            best_score = new_score

        if amounts[-1] == TEASPOONS:
            break

        # Find rightmost index that has something to the left.
        for i in range(1, len(amounts)):
            if amounts[i - 1] != 0:
                inc = i

        # Take one from the left, and gather everything from the right.
        amounts[inc] += 1
        amounts[inc - 1] -= 1
        for i in range(inc + 1, len(amounts)):
            amounts[inc] += amounts[i]
            amounts[i] = 0

    print("Best score with {} calories: {}".format(500, best_score))


part1()
part2()
