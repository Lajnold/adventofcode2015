#!/usr/bin/env python3

with open("day9-input.txt") as f:
    # place1 to place2 = 53
    day9_input_lines = f.read().split("\n")


def get_shortest_from(from_idx, places, distances, visited, pick):
    from_place = places[from_idx]
    shortest = None

    for via_idx in range(len(places)):
        if via_idx in visited:
            continue

        via_place = places[via_idx]
        via_dist = next(d[2] for d in distances if {d[0], d[1]} == {from_place, via_place})
        via_visited = visited + [via_idx]
        via_shortest = get_shortest_from(via_idx, places, distances, via_visited, pick)
        via_total = via_dist + via_shortest
        shortest = via_total if shortest is None else pick(via_total, shortest)

    return shortest if shortest is not None else 0

def get_shortest(places, distances, pick):
    shortest = None

    for i in range(len(places)):
        visited = [i]
        i_shortest = get_shortest_from(i, places, distances, visited, pick)
        shortest = i_shortest if shortest is None else pick(i_shortest, shortest)

    return shortest

def parse_day9_input(lines):
    distances = []
    all_places = []
    for line in lines:
        places, distance = line.split(" = ")
        place1, place2 = places.split(" to ")
        distances.append((place1, place2, int(distance)))
        all_places.append(place1)
        all_places.append(place2)

    all_places = list(set(all_places))
    return (all_places, distances)

def part1():
    pick = lambda x, y: x if x < y else y
    all_places, distances = parse_day9_input(day9_input_lines)
    shortest = get_shortest(all_places, distances, pick)
    print("Shortest distance: {}".format(shortest))

def part2():
    pick = lambda x, y: x if x > y else y
    all_places, distances = parse_day9_input(day9_input_lines)
    shortest = get_shortest(all_places, distances, pick)
    print("Shortest distance: {}".format(shortest))

part1()
part2()
