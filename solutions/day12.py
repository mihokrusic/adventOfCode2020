import math

def __get_direction_delta(direction):
    if direction == 0:
        return [0, -1]
    if direction == 1:
        return [1, 0]
    if direction == 2:
        return [0, 1]
    if direction == 3:
        return [-1, 0]
    return

def part1(input):
    current = [0, 0]
    direction = 1
    for line in input:
        command = line[0:1]
        amount = int(line[1:])

        if command == "N":
            current[1] -= amount
        if command == "S":
            current[1] += amount
        if command == "W":
            current[0] -= amount
        if command == "E":
            current[0] += amount
        if command == "F":
            direction_delta = __get_direction_delta(direction)
            current[0] += amount * direction_delta[0]
            current[1] += amount * direction_delta[1]
        if command == "L":
            direction = ((direction + int(-amount / 90)) + 4) % 4
        if command == "R":
            direction = ((direction + int(+amount / 90)) + 4) % 4

    return abs(current[0]) + abs(current[1])

def part2(input):
    current = [0, 0]
    waypoint = [10, -1]
    quadrant = 0
    for line in input:
        new_quadrant = quadrant
        quadrant_diff = 0
        command = line[0:1]
        move_direction = command
        amount = int(line[1:])

        if command == "F":
            current[0] += (waypoint[0]) * amount
            current[1] += (waypoint[1]) * amount
        if command == "N":
            waypoint[1] -= amount
        if command == "S":
            waypoint[1] += amount
        if command == "W":
            waypoint[0] -= amount
        if command == "E":
            waypoint[0] += amount

        if command == "L":
            amount = amount % 360
            new_quadrant = ((quadrant + int(-amount / 90)) + 4) % 4
            quadrant_diff = math.floor(amount / 90)

            if quadrant_diff == 3:
                quadrant_diff = 1
                move_direction = "R"

        if command == "R":
            amount = amount % 360

            new_quadrant = ((quadrant + int(amount / 90)) + 4) % 4
            quadrant_diff = math.floor(amount / 90)

            if quadrant_diff == 3:
                quadrant_diff = 1
                move_direction = "L"

        if new_quadrant != quadrant:
            if quadrant_diff == 2:
                waypoint = [-waypoint[0], -waypoint[1]]
            else:
                waypoint = [waypoint[1], -waypoint[0]] if move_direction == 'L' else [-waypoint[1], waypoint[0]]

        quadrant = new_quadrant

    return abs(current[0]) + abs(current[1])