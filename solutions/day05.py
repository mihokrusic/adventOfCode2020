import math

def get_seat_id(input):
    start_row = 0
    end_row = 127
    start_seat = 0
    end_seat = 7
    for i in range(7):
        if input[i] == 'F':
            end_row = start_row + math.floor((end_row - start_row) / 2)
        if input[i] == 'B':
            start_row = start_row + math.floor((end_row - start_row) / 2) + 1

    for i in range(3):
        if input[i + 7] == 'L':
            end_seat = start_seat + math.floor((end_seat - start_seat) / 2)
        if input[i + 7] == 'R':
            start_seat = start_seat + math.floor((end_seat - start_seat) / 2) + 1

    return start_row * 8 + start_seat

def part1(input):
    highest_seat_id = -1

    for line in input:
        current = get_seat_id(line)
        if (current > highest_seat_id):
            highest_seat_id = current

    return highest_seat_id


def part2(input):
    lowest_seat_id = 99999999999
    highest_seat_id = -1

    seats = set()

    for line in input:
        current = get_seat_id(line)
        seats.add(current)
        if (current > highest_seat_id):
            highest_seat_id = current
        if (current < lowest_seat_id):
            lowest_seat_id = current

    for i in range(lowest_seat_id, highest_seat_id + 1):
        if not i in seats:
            return i

    return -1