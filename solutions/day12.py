import math

def __get_direction_vector(direction):
    if direction == 0:
        return (0, -1)
    if direction == 1:
        return (1, 0)
    if direction == 2:
        return (0, 1)
    if direction == 3:
        return (-1, 0)
    return None

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
            x_delta, y_delta = __get_direction_vector(direction)
            current[0] += amount * x_delta
            current[1] += amount * y_delta
        if command == "L":
            direction = (direction + int(-amount / 90) + 4) % 4
        if command == "R":
            direction = (direction + int(+amount / 90) + 4) % 4

    return abs(current[0]) + abs(current[1])

def part2(input):
    current = [0, 0]
    waypoint = [10, -1]
    quadrant = 0
    for line in input:
        command = line[0:1]
        amount = int(line[1:])

        quadrant_delta = 0
        move_direction = command

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

        if command == "R" or command == "L":
            amount = amount % 360
            quadrant_delta = math.floor(amount / 90)

            if command == "L":
                quadrant = (quadrant - quadrant_delta + 4) % 4
            else:
                quadrant = (quadrant + quadrant_delta + 4) % 4

            if quadrant_delta == 3:
                if command == "R":
                    move_direction = "L"
                else:
                    move_direction = "R"
                quadrant_delta = 1

        if quadrant_delta > 0:
            if quadrant_delta == 2:
                waypoint = [-waypoint[0], -waypoint[1]]
            else:
                waypoint = [waypoint[1], -waypoint[0]] if move_direction == 'L' else [-waypoint[1], waypoint[0]]

    return abs(current[0]) + abs(current[1])