#!/usr/bin/env python3

with open("day13-input.txt") as f:
    day13_input = f.read()
    day13_input_lines = day13_input.split("\n")

def parse_score(line):
    # Alice would gain 54 happiness units by sitting next to Bob.
    split = line.rstrip(".").split()
    p1, gain, quantity, p2 = split[0], split[2], int(split[3]), split[-1]
    if gain == "lose":
        quantity = -quantity;
    return (p1, p2, quantity)

def parse_scores(lines):
    return [parse_score(line) for line in lines]

def get_people_from_scores(scores):
    people = []
    for sc in scores:
        people.append(sc[0])
        people.append(sc[1])
    return [p for p in set(people)]

def get_happiness_for_combination(p1, p2, scores):
    sc = next(filter(lambda x: x[0] == p1 and x[1] == p2, scores))
    return sc[2]

def calculate_happiness(arrangement, scores):
    total = 0
    for i in range(len(arrangement)):
        prev_i = i - 1 if i > 0 else len(arrangement) - 1
        next_i = i + 1 if i < len(arrangement) - 1 else 0
        total += get_happiness_for_combination(arrangement[i], arrangement[prev_i], scores)
        total += get_happiness_for_combination(arrangement[i], arrangement[next_i], scores)
    return total

def find_best_arrangement(arrangement_so_far, people, scores):
    if len(arrangement_so_far) == len(people):
        return calculate_happiness(arrangement_so_far, scores)

    people_to_test = (p for p in people if p not in arrangement_so_far)
    max_happiness = None

    for p in people_to_test:
        new_arrangement = arrangement_so_far + [p]
        new_arrangement_happiness = find_best_arrangement(new_arrangement, people, scores)

        if max_happiness is None or new_arrangement_happiness > max_happiness:
            max_happiness = new_arrangement_happiness

    return max_happiness

def part1():
    scores = parse_scores(day13_input_lines)
    people = get_people_from_scores(scores)
    max_happiness = find_best_arrangement([], people, scores)
    print("Max happiness change: {}".format(max_happiness))


def part2():
    def add_me_to_scores(people, scores):
        new_scores = list(scores)
        for p in people:
            new_scores.append(("Me", p, 0))
            new_scores.append((p, "Me", 0))
        return new_scores

    scores = parse_scores(day13_input_lines)
    people = get_people_from_scores(scores)

    scores_with_me = add_me_to_scores(people, scores)
    people_with_me = people + ["Me"]

    max_happiness = find_best_arrangement([], people_with_me, scores_with_me)
    print("Max happiness change with me seated: {}".format(max_happiness))

part1()
part2()
