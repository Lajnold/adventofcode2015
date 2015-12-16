#!/usr/bin/env python3

import json

with open("day12-input.txt") as f:
    day12_input = f.read()
    day12_input_json = json.loads(day12_input)


def is_int(token):
    return isinstance(token, int)

def is_list(token):
    return isinstance(token, list)

def is_dict(token):
    return isinstance(token, dict)


def part1():
    def crawl(x):
        if is_int(x):
            return x
        elif is_list(x):
            return sum(crawl(el) for el in x)
        elif is_dict(x):
            return sum(crawl(el) for el in x.values())
        else:
            return 0

    input_sum = crawl(day12_input_json)
    print("Sum of numbers: {}".format(input_sum))


def part2():
    def has_forbidden_value(x):
        return "red" in x.values()

    def crawl(x):
        if is_int(x):
            return x
        elif is_list(x):
            return sum(crawl(el) for el in x)
        elif is_dict(x) and not has_forbidden_value(x):
            return sum(crawl(el) for el in x.values())
        else:
            return 0

    input_sum = crawl(day12_input_json)
    print("Sum of numbers: {}".format(input_sum))


part1()
part2()
