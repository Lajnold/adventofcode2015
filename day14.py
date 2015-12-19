#!/usr/bin/env python3

with open("day14-input.txt") as f:
    day14_input = f.read()
    day14_input_lines = day14_input.split("\n")

def parse_reindeer(line):
    # Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.
    split = line.rstrip(".").split(" ")
    name, speed, speed_time, rest_time = split[0], int(split[3]), int(split[6]), int(split[-2])
    return (name, speed, speed_time, rest_time)

def parse_reindeers(lines):
    return [parse_reindeer(line) for line in lines]

def part1():
    seconds = 2503
    reindeer_specs = parse_reindeers(day14_input_lines)

    distances = {}
    for spec in reindeer_specs:
        period_length = spec[2] + spec[3]
        num_full_periods = seconds // period_length
        rest_seconds = seconds - (num_full_periods * period_length)
        rest_speed_seconds = min(spec[2], rest_seconds)
        full_periods_dist = num_full_periods * spec[2] * spec[1]
        rest_periods_dist = rest_speed_seconds * spec[1]
        distances[spec[0]] = full_periods_dist + rest_periods_dist

    print("Winning distance: {}".format(max(distances.values())))

def part2():
    seconds = 2503
    reindeer_specs = parse_reindeers(day14_input_lines)

    distances = {r[0]: 0 for r in reindeer_specs}
    points = {r[0]: 0 for r in reindeer_specs}
    for s in range(seconds):
        for spec in reindeer_specs:
            period_length = spec[2] + spec[3]
            num_full_periods = s // period_length
            rest_seconds = s - (num_full_periods * period_length)
            if rest_seconds < spec[2]:
                distances[spec[0]] += spec[1]

        max_dist = None
        for spec in reindeer_specs:
            dist = distances[spec[0]]
            if max_dist is None or dist > max_dist[1]:
                max_dist = (spec[0], dist)

        points[max_dist[0]] += 1

    print("Winning points: {}".format(max(points.values())))

part1()
part2()
