#!/usr/bin/env python3

day20_input = 34000000


def number_of_presents_part1(house):
    return sum(elf * 10 for elf in range(1, house + 1) if house % elf == 0)


def number_of_presents_part2(house):
    return sum(elf * 11 for elf in range(1, house + 1) if house % elf == 0 and house // elf <= 50)


def part1():
    house = 1
    high = -1

    while high < day20_input:
        presents = number_of_presents_part1(house)

        if presents > high:
            high = presents
            print("New high: {} at house: {}".format(high, house))

        if presents < day20_input:
            house += 1

    print("House: {}".format(house))


def part2():
    house = 1
    high = -1

    while high < day20_input:
        presents = number_of_presents_part2(house)

        if presents > high:
            high = presents
            print("New high: {} at house: {}".format(high, house))

        if presents < day20_input:
            house += 1

    print("House: {}".format(house))


part1()
part2()
