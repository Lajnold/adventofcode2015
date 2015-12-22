#!/usr/bin/env python3

with open("day18-input.txt") as f:
    day18_input_lines = f.read().split("\n")


def parse_bulb(char):
    # '#' is on, '.' is off.
    return 1 if char == "#" else 0

def parse_row(line):
    # ##.#...#
    return list(map(parse_bulb, line))

def parse_grid(lines):
    # ##.#...#
    # .##..##.
    # ###..#.#
    return list(map(parse_row, lines))


def count_neighbours_on(grid, i_row, i_col):
    num_neighbours_on = 0
    num_cols = len(grid[0])

    if i_row > 0:
        num_neighbours_on += grid[i_row - 1][i_col]

        if i_col > 0:
            num_neighbours_on += grid[i_row - 1][i_col - 1]
        if i_col < num_cols - 1:
            num_neighbours_on += grid[i_row - 1][i_col + 1]

    if i_row < len(grid) - 1:
        num_neighbours_on += grid[i_row + 1][i_col]

        if i_col > 0:
            num_neighbours_on += grid[i_row + 1][i_col - 1]
        if i_col < num_cols - 1:
            num_neighbours_on += grid[i_row + 1][i_col + 1]

    if i_col > 0:
        num_neighbours_on += grid[i_row][i_col - 1]
    if i_col < num_cols - 1:
        num_neighbours_on += grid[i_row][i_col + 1]

    return num_neighbours_on


def part1():
    def animate_one_step(grid):
        new_grid = []

        for i_row in range(len(grid)):
            new_row = []
            new_grid.append(new_row)

            for i_col in range(len(grid[i_row])):
                num_neighbours_on = count_neighbours_on(grid, i_row, i_col)

                if grid[i_row][i_col] == 0:
                    if num_neighbours_on == 3:
                        new_row.append(1)
                    else:
                        new_row.append(0)
                else:
                    if num_neighbours_on == 2 or num_neighbours_on == 3:
                        new_row.append(1)
                    else:
                        new_row.append(0)

        return new_grid


    grid = parse_grid(day18_input_lines)
    for row in range(100):
        grid = animate_one_step(grid)

    num_lights_on = sum(bulb for row in grid for bulb in row)
    print("Lights on: {}".format(num_lights_on))


def part2():
    def turn_on_corners(grid):
        num_rows = len(grid)
        num_columns = len(grid[0])

        grid[0][0] = 1
        grid[0][num_columns - 1] = 1
        grid[num_rows - 1][0] = 1
        grid[num_rows - 1][num_columns - 1] = 1


    def animate_one_step(grid):
        num_rows = len(grid)
        num_columns = len(grid[0])
        new_grid = []

        for i_row in range(len(grid)):
            new_row = []
            new_grid.append(new_row)

            for i_col in range(len(grid[i_row])):
                is_corner = \
                    (i_row == 0 or i_row == num_rows - 1) and \
                    (i_col == 0 or i_col == num_columns - 1)

                if is_corner:
                    new_row.append(1)
                else:
                    num_neighbours_on = count_neighbours_on(grid, i_row, i_col)

                    if grid[i_row][i_col] == 0:
                        if num_neighbours_on == 3:
                            new_row.append(1)
                        else:
                            new_row.append(0)
                    else:
                        if num_neighbours_on == 2 or num_neighbours_on == 3:
                            new_row.append(1)
                        else:
                            new_row.append(0)

        return new_grid


    grid = parse_grid(day18_input_lines)
    turn_on_corners(grid)

    for row in range(100):
        grid = animate_one_step(grid)

    num_lights_on = sum(bulb for row in grid for bulb in row)
    print("Lights on: {}".format(num_lights_on))


part1()
part2()
