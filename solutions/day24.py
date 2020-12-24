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

def get_black_adjacent(field, pos):
    result = 0
    adj_key = (pos[0] + 1, pos[1] - 1, pos[2])
    if adj_key in field:
        result += 1
    adj_key = (pos[0] - 1, pos[1] + 1, pos[2])
    if adj_key in field:
        result += 1
    adj_key = (pos[0] + 1, pos[1], pos[2] - 1)
    if adj_key in field:
        result += 1
    adj_key = (pos[0] - 1, pos[1], pos[2] + 1)
    if adj_key in field:
        result += 1
    adj_key = (pos[0], pos[1] - 1, pos[2] + 1)
    if adj_key in field:
        result += 1
    adj_key = (pos[0], pos[1] + 1, pos[2] - 1)
    if adj_key in field:
        result += 1
    return result


def solve(input, part):
    field = set()
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
        if key not in field:
            field.add(key)
        else:
            field.remove(key)

    if part == 1:
        return len(field)
    for ix in range(100):
        new_field = copy.deepcopy(field)
        for key in field:
            blacks_adjacent = get_black_adjacent(field, key)
            if key not in field and blacks_adjacent == 2:
                field.add(key)
            else:
                if key in field and (blacks_adjacent == 0 or blacks_adjacent > 2):
                    new_field.remove(key)
                adj_key = (key[0] + 1, key[1] - 1, key[2])
                if adj_key not in field:
                    blacks_adjacent = get_black_adjacent(field, adj_key)
                    if blacks_adjacent == 2:
                        new_field.add(adj_key)
                adj_key = (key[0] - 1, key[1] + 1, key[2])
                if adj_key not in field:
                    blacks_adjacent = get_black_adjacent(field, adj_key)
                    if blacks_adjacent == 2:
                        new_field.add(adj_key)
                adj_key = (key[0] + 1, key[1], key[2] - 1)
                if adj_key not in field:
                    blacks_adjacent = get_black_adjacent(field, adj_key)
                    if blacks_adjacent == 2:
                        new_field.add(adj_key)
                adj_key = (key[0] - 1, key[1], key[2] + 1)
                if adj_key not in field:
                    blacks_adjacent = get_black_adjacent(field, adj_key)
                    if blacks_adjacent == 2:
                        new_field.add(adj_key)
                adj_key = (key[0], key[1] - 1, key[2] + 1)
                if adj_key not in field:
                    blacks_adjacent = get_black_adjacent(field, adj_key)
                    if blacks_adjacent == 2:
                        new_field.add(adj_key)
                adj_key = (key[0], key[1] + 1, key[2] - 1)
                if adj_key not in field:
                    blacks_adjacent = get_black_adjacent(field, adj_key)
                    if blacks_adjacent == 2:
                        new_field.add(adj_key)

        field = new_field
    return len(field)
