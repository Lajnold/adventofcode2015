#!/usr/bin/env python3

from collections import deque

with open("day19-input.txt") as f:
    day19_input_lines = f.read().split("\n")


def parse_rule(line):
    # Al => ThF
    lhs, rhs = line.split(" => ")
    return lhs, rhs


def parse_input_file(lines):
    rules = list(map(parse_rule, lines[:-2]))
    return rules, lines[-1]


def find_next_atom_bounds(molecule, prev_end):
    start = prev_end
    end = start + 1
    while end < len(molecule) and molecule[end].islower():
        end += 1
    return [start, end]


def find_rules_for_atom(atom, rules):
    return (x for x in rules if x[0] == atom)


def apply_rule(molecule, atom_start, atom_end, rule):
    return molecule[0:atom_start] + rule[1] + molecule[atom_end:]


def part1():
    rules, molecule = parse_input_file(day19_input_lines)

    productions = set()

    atom_end = 0
    while atom_end < len(molecule):
        atom_start, atom_end = find_next_atom_bounds(molecule, atom_end)
        atom = molecule[atom_start:atom_end]
        for rule in find_rules_for_atom(atom, rules):
            new_molecule = apply_rule(molecule, atom_start, atom_end, rule)
            productions.add(new_molecule)

    print("Distinct molecules: {}".format(len(productions)))


def part2():
    pass


part1()
part2()
