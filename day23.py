#!/usr/bin/env python3

with open('day23-input.txt') as f:
    day23_input_lines = f.read().split("\n")


def parse_instructions(lines):
    return [line.replace(",", "").split() for line in lines]


def run_instructions(instructions, registers):
    addr = 0
    while addr < len(instructions):
        line = instructions[addr]
        instr = line[0]

        if instr == "hlf":
            reg = line[1]
            registers[reg] //= 2
            addr += 1
        elif instr == "tpl":
            reg = line[1]
            registers[reg] *= 3
            addr += 1
        elif instr == "inc":
            reg = line[1]
            registers[reg] += 1
            addr += 1
        elif instr == "jmp":
            offset = int(line[1])
            addr += offset
        elif instr == "jie":
            reg = line[1]
            offset = int(line[2])
            if registers[reg] % 2 == 0:
                addr += offset
            else:
                addr += 1
        elif instr == "jio":
            reg = line[1]
            offset = int(line[2])
            if registers[reg] == 1:
                addr += offset
            else:
                addr += 1


def part1():
    instructions = parse_instructions(day23_input_lines)
    registers = {"a": 0, "b": 0}

    run_instructions(instructions, registers)

    print("Registers: {}".format(registers))


def part2():
    instructions = parse_instructions(day23_input_lines)
    registers = {"a": 1, "b": 0}
    
    run_instructions(instructions, registers)

    print("Registers: {}".format(registers))


part1()
part2()
