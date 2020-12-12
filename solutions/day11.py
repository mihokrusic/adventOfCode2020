import copy

def __get_seat_value(seats, y, x, y_delta, x_delta, adjacent):
    if adjacent:
        return seats[y + y_delta][x + x_delta]

    new_x = x + x_delta
    new_y = y + y_delta
    while 0 <= new_x < len(seats[0]) and 0 <= new_y < len(seats):
        if seats[new_y][new_x] != ".":
            return seats[new_y][new_x]
        new_x += x_delta
        new_y += y_delta

    return '.'

def __check_neighbours_state(seats, y, x, state, adjacent):
    result = 0
    if (y != 0 and x != 0):
        result += int(__get_seat_value(seats, y, x, -1, -1, adjacent) == state)
    if (y != 0):
        result += int(__get_seat_value(seats, y, x, -1, 0, adjacent) == state)
    if (y != 0 and x != len(seats[y]) - 1):
        result += int(__get_seat_value(seats, y, x, -1, 1, adjacent) == state)
    if (x != 0):
        result += int(__get_seat_value(seats, y, x, 0, -1, adjacent) == state)
    if (x != len(seats[y]) - 1):
        result += int(__get_seat_value(seats, y, x, 0, 1, adjacent) == state)
    if (y != len(seats) - 1 and x != 0):
        result += int(__get_seat_value(seats, y, x, 1, -1, adjacent) == state)
    if (y != len(seats) - 1):
        result += int(__get_seat_value(seats, y, x, 1, 0, adjacent) == state)
    if (y != len(seats) - 1 and x != len(seats[y]) - 1):
        result += int(__get_seat_value(seats, y, x, 1, 1, adjacent) == state)

    return result

def __get_occupied(seats):
    result = 0
    for y in range(len(seats)):
        for x in range(len(seats[y])):
            result += 1 if seats[y][x] == "#" else 0

    return result


def part1(input):
    seats = [[x for x in y.rstrip()] for y in input]
    while True:
        changed = False
        new_seats = copy.deepcopy(seats)
        for y in range(len(seats)):
            for x in range(len(seats[y])):
                if seats[y][x] == "L":
                    occupied_neighbours = __check_neighbours_state(seats, y, x, "#", True)
                    if occupied_neighbours == 0 and new_seats[y][x] != "#":
                        new_seats[y][x] = "#"
                        changed = True

                if seats[y][x] == "#":
                    occupied_neighbours = __check_neighbours_state(seats, y, x, "#", True)
                    if occupied_neighbours >= 4 and new_seats[y][x] != "L":
                        new_seats[y][x] = "L"
                        changed = True

        seats = new_seats
        if not changed:
            break
    return __get_occupied(seats)


def part2(input):
    seats = [[x for x in y.rstrip()] for y in input]
    while True:
        changed = False
        new_seats = copy.deepcopy(seats)
        for y in range(len(seats)):
            for x in range(len(seats[y])):
                if seats[y][x] == "L":
                    occupied_neighbours = __check_neighbours_state(seats, y, x, "#", False)
                    if occupied_neighbours == 0 and new_seats[y][x] != "#":
                        new_seats[y][x] = "#"
                        changed = True

                if seats[y][x] == "#":
                    occupied_neighbours = __check_neighbours_state(seats, y, x, "#", False)
                    if occupied_neighbours >= 5 and new_seats[y][x] != "L":
                        new_seats[y][x] = "L"
                        changed = True

        seats = new_seats
        if not changed:
            break
    return __get_occupied(seats)