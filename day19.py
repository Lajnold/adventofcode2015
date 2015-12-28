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
    return (start, end)

def find_all_atom_bounds(molecule):
    bounds = []
    start, end = find_next_atom_bounds(molecule, 0)
    while start < len(molecule):
        bounds.append((start, end))
        start, end = find_next_atom_bounds(molecule, end)
    return bounds


def find_rules_from_atom(atom, rules):
    return (rule for rule in rules if rule[0] == atom)

def find_rule_creating_molecule(molecule, rules):
    matching = (rule for rule in rules if rule[1] == molecule)
    return next(matching, None)


def apply_rule(molecule, replace_start, replace_end, rule):
    return molecule[:replace_start] + rule[1] + molecule[replace_end:]

def inverse_apply_rule(molecule, replace_start, replace_end, rule):
    return molecule[:replace_start] + rule[0] + molecule[replace_end:]


def part1():
    rules, molecule = parse_input_file(day19_input_lines)

    productions = set()
    for atom_start, atom_end in find_all_atom_bounds(molecule):
        atom = molecule[atom_start:atom_end]
        for rule in find_rules_from_atom(atom, rules):
            new_molecule = apply_rule(molecule, atom_start, atom_end, rule)
            productions.add(new_molecule)

    print("Distinct molecules: {}".format(len(productions)))


def part2():
    rules, molecule = parse_input_file(day19_input_lines)

    max_rhs = max(len(find_all_atom_bounds(rule[1])) for rule in rules)

    created_molecules = set()
    result_count = None

    steps = deque()
    steps.append((molecule, 0))

    while result_count is None:
        step_molecule, step_count = steps.pop()

        atom_bounds = find_all_atom_bounds(step_molecule)
        for start_idx in range(len(atom_bounds)):
            for end_idx in range(start_idx, min(len(atom_bounds), start_idx + max_rhs)):
                submolecule_start = atom_bounds[start_idx][0]
                submolecule_end = atom_bounds[end_idx][1]
                submolecule = step_molecule[submolecule_start:submolecule_end]
                rule = find_rule_creating_molecule(submolecule, rules)

                if rule is not None:
                    new_molecule = inverse_apply_rule(step_molecule, submolecule_start, submolecule_end, rule)

                    if new_molecule not in created_molecules:
                        steps.append((new_molecule, step_count + 1))
                        created_molecules.add(new_molecule)

                        if new_molecule == "e":
                            result_count = step_count + 1

    print("Steps to make medicine: {}".format(result_count))


#part1()
part2()
