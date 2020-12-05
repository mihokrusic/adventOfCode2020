import math

def get_seat_id(input):
    rows = [0, 127]
    seats = [0, 7]
    for i in range(7):
        new_limit = rows[0] + math.floor((rows[1] - rows[0]) / 2)
        if input[i] == 'F':
            rows[1] = new_limit
        else:
            rows[0] = new_limit + 1

    for i in range(7, 10):
        new_limit = seats[0] + math.floor((seats[1] - seats[0]) / 2)
        if input[i] == 'L':
            seats[1] = new_limit
        else:
            seats[0] = new_limit + 1

    return rows[0] * 8 + seats[0]

def part1(input):
    highest_seat_id = None

    for line in input:
        current = get_seat_id(line)
        if (highest_seat_id == None or current > highest_seat_id):
            highest_seat_id = current

    return highest_seat_id


def part2(input):
    lowest_seat_id = None
    highest_seat_id = None

    seats = set()

    for line in input:
        current = get_seat_id(line)
        seats.add(current)
        if (highest_seat_id == None or current > highest_seat_id):
            highest_seat_id = current

        if (lowest_seat_id == None or current < lowest_seat_id):
            lowest_seat_id = current

    for i in range(lowest_seat_id, highest_seat_id + 1):
        if not i in seats:
            return i

    return -1