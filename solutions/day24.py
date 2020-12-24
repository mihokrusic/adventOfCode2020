import copy
import numpy as np

movements = {
    'w': [-1, 1, 0],
    'e': [1, -1, 0],
    'nw': [0, 1, -1],
    'se': [0, -1, 1],
    'sw': [-1, 0, 1],
    'ne': [1, 0, -1],
}

def get_blacks(field):
    blacks = 0
    for key in field.keys():
        if field[key] == 1:
            blacks+=1
    return blacks

def get_black_adjacent(field, pos):
    result = 0
    adj_key = (pos[0] + 1, pos[1] - 1, pos[2])
    if adj_key in field and field[adj_key] == 1:
        result += 1
    adj_key = (pos[0] - 1, pos[1] + 1, pos[2])
    if adj_key in field and field[adj_key] == 1:
        result += 1
    adj_key = (pos[0] + 1, pos[1], pos[2] - 1)
    if adj_key in field and field[adj_key] == 1:
        result += 1
    adj_key = (pos[0] - 1, pos[1], pos[2] + 1)
    if adj_key in field and field[adj_key] == 1:
        result += 1
    adj_key = (pos[0], pos[1] - 1, pos[2] + 1)
    if adj_key in field and field[adj_key] == 1:
        result += 1
    adj_key = (pos[0], pos[1] + 1, pos[2] - 1)
    if adj_key in field and field[adj_key] == 1:
        result += 1
    return result


def solve(input, part):
    field = dict()
    dims = np.zeros(6, dtype=int)
    for line in input.split('\n'):
        # x, y, z
        pos = np.array([0, 0, 0])
        ix = 0
        while ix < len(line.rstrip()):
            move = ''
            move_ix = 0
            if line[ix] == 'w' or line[ix] == 'e':
                move_ix = 1
            else:
                move_ix = 2

            move = line[ix:ix+move_ix]
            pos += movements[move]
            ix += move_ix

        key = tuple(pos)
        field[key] = 1 if key not in field else  1 - field[key]

        dims[0] = min(pos[0], dims[0])
        dims[1] = max(pos[0], dims[1])
        dims[2] = min(pos[1], dims[2])
        dims[3] = max(pos[1], dims[3])
        dims[4] = min(pos[2], dims[4])
        dims[5] = max(pos[2], dims[5])

    if part == 1:
        return get_blacks(field)

    for ix in range(100):
        new_field = copy.deepcopy(field)
        for x in range(dims[0] - 1, dims[1] + 2):
            for y in range(dims[2] - 1, dims[3] + 2):
                for z in range(dims[4] - 1, dims[5] + 2):
                    pos = (x, y, z)
                    blacks_adjacent = get_black_adjacent(field, pos)
                    if (pos not in field or field[pos] == 0) and blacks_adjacent == 2:
                        new_field[pos] = 1
                    if pos in field and field[pos] == 1 and (blacks_adjacent == 0 or blacks_adjacent > 2):
                        new_field[pos] = 0

        # dims[0] = dims[0] - 1
        # dims[1] = dims[1] + 1
        # dims[2] = dims[2] - 1
        # dims[3] = dims[3] + 1
        # dims[4] = dims[4] - 1
        # dims[5] = dims[5] + 1
        field = new_field
    return get_blacks(field)
