#!/usr/bin/env python3

with open("day16-input.txt") as f:
    day16_input = f.read()
    day16_input_lines = day16_input.split("\n")

analysis_result = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}


def parse_aunt(line):
    # Sue 1: goldfish: 9, cars: 0, samoyeds: 9
    split = line.split(": ", 1)
    name_line = split[0]
    props_line = split[1]

    num = name_line.split()[1]

    props = {}
    for prop in props_line.split(", "):
        prop_split = prop.split(": ")
        k, v = prop_split[0], int(prop_split[1])
        props[k] = v

    return (num, props)

def parse_aunts(lines):
    return list(map(parse_aunt, lines))

def part1():
    def get_matching_aunts(prop, val, aunts):
        return [aunt for aunt in aunts if aunt[1].get(prop, val) == val]

    aunts = parse_aunts(day16_input_lines)

    matches = list(aunts)
    for k, v in analysis_result.items():
        prop_matches = get_matching_aunts(k, v, aunts)
        matches = [m for m in matches if m in prop_matches]

    print("Aunt: {}".format(matches[0][0]))

def part2():
    GT_PROPS = ["cats", "trees"]
    LT_PROPS = ["pomeranians", "goldfish"]

    def get_matching_aunts(prop, val, aunts):
        if prop in GT_PROPS:
            return [aunt for aunt in aunts if aunt[1].get(prop, val + 1) > val]
        elif prop in LT_PROPS:
            return [aunt for aunt in aunts if aunt[1].get(prop, val - 1) < val]
        else:
            return [aunt for aunt in aunts if aunt[1].get(prop, val) == val]

    aunts = parse_aunts(day16_input_lines)

    matches = list(aunts)
    for k, v in analysis_result.items():
        prop_matches = get_matching_aunts(k, v, aunts)
        matches = [m for m in matches if m in prop_matches]

    print("Real aunt: {}".format(matches[0][0]))

part1()
part2()
