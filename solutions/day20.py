#!/usr/bin/env python3
import re
import numpy as np
from math import sqrt
from numpy.core.defchararray import title

monster = """                  #
#    ##    ##    ###
 #  #  #  #  #  #   """

def get_next_tile_with_hash(hash, tile_hashes, ignore_id):
    for th in tile_hashes:
        if th[0] == ignore_id:
            continue

        if hash in th[1]:
            return th[0], th[1].index(hash)

    return -1

def rotate_flip_next_tile(next_tile, next_hash_ix, normal_offset, flip_offset):
    if 0 <= next_hash_ix < 4:
        next_tile = np.flip(np.array(next_tile), 1)
        rot_times = next_hash_ix - normal_offset
        if rot_times != 0:
            next_tile = np.rot90(np.array(next_tile), -rot_times)
    else:
        rot_times = next_hash_ix - flip_offset
        if rot_times != 0:
            next_tile = np.rot90(np.array(next_tile), -rot_times)
    return next_tile

def get_border_hash(tile):
    t = tile[0]
    r = [y[-1] for y in tile]
    b = list(reversed(tile[-1]))
    l = list(reversed([y[0] for y in tile]))

    return (
        int(''.join(t).replace('#', '1').replace('.', '0'),2),
        int(''.join(r).replace('#', '1').replace('.', '0'),2),
        int(''.join(b).replace('#', '1').replace('.', '0'),2),
        int(''.join(l).replace('#', '1').replace('.', '0'),2)
    )

def get_image(tiles, tile_hashes, corners, corners_found_elems):
    image_side = int(sqrt(len(tiles.keys())))

    image = [[[] for _ in range(image_side)] for _ in range(image_side)]
    image_ids = [[0 for _ in range(image_side)] for _ in range(image_side)]
    for i in range(0, image_side):
        if i == 0:
            first_corner_id = corners[0][0]
            first_corner_tile = np.array(tiles[corners[0][0]])
            # blah
            if (corners_found_elems[0] == [0, 1]):
                first_corner_tile = np.rot90(first_corner_tile, -1)
            if (corners_found_elems[0] == [1, 2]):
                pass
            if (corners_found_elems[0] == [2, 3]):
                first_corner_tile = np.rot90(first_corner_tile, 1)
            if (corners_found_elems[0] == [0, 3]):
                first_corner_tile = np.rot90(first_corner_tile, 2)
            image_ids[0][0] = first_corner_id
            image[0][0] = np.array(first_corner_tile)
        else:
            current_tile_id = image_ids[i - 1][0]
            current_tile = image[i - 1][0]
            current_hash = get_border_hash(current_tile)[2]
            next_tile_id, next_hash_ix = get_next_tile_with_hash(current_hash, tile_hashes, current_tile_id)

            next_tile = rotate_flip_next_tile(np.array(tiles[next_tile_id]), next_hash_ix, 0, 4)
            image_ids[i][0] = next_tile_id
            image[i][0] = next_tile

        for j in range(1, image_side):
            current_tile_id = image_ids[i][j - 1]
            current_tile = image[i][j - 1]
            current_hash = get_border_hash(current_tile)[1]
            next_tile_id, next_hash_ix = get_next_tile_with_hash(current_hash, tile_hashes, current_tile_id)

            next_tile = rotate_flip_next_tile(np.array(tiles[next_tile_id]), next_hash_ix, 1, 5)
            image_ids[i][j] = next_tile_id
            image[i][j] = next_tile

    for row in image:
        for ix, tile in enumerate(row):
            row[ix] = tile[1:-1, 1:-1]

    image_concat = []
    for row in image:
        row_all = np.concatenate(row)
        image_concat.extend(np.concatenate(row, axis=1))

    return image_concat

def check_for_monsters(image):
    matches = 0
    for ix in range(1, len(image) - 1):
        line_above = ''.join(image[ix - 1])
        line = ''.join(image[ix])
        line_below = ''.join(image[ix + 1])
        mid_hits = re.finditer(r'#.{4}##.{4}##.{4}###', line)
        for mid_hit in mid_hits:
            above = False
            below = False
            mid_hit_pos = mid_hit.span()
            if line_above[mid_hit_pos[0] + 18] == '#':
                above = True
            below_hits = re.finditer(r'(?=.{1}#.{2}#.{2}#.{2}#.{2}#.{2}#.{3})', line_below)
            for bh in below_hits:
                below_hit_pos = bh.span()
                if below_hit_pos[0] == mid_hit_pos[0]:
                    below = True

            if above and below:
                matches += 1

    return matches

def solve(input, part):
    tiles = dict()
    for tile in input.split('\n\n'):
        tile_lines = tile.split('\n')
        tile_id = tile_lines[0].strip('Tile ').strip(':')
        tiles[tile_id] = [list(line.rstrip()) for line in tile_lines[1:]]

    borders = []
    tile_hashes = []
    for key in tiles:
        tile = tiles[key]
        normal_hash = get_border_hash(tile)

        flip_tile = np.flip(np.array(tile), 1)
        fliped_hash = get_border_hash(flip_tile)
        tile_hashes.append((key, [*normal_hash, *fliped_hash]))
        borders.extend(normal_hash)
        borders.extend(fliped_hash)

    corners = []
    corners_found_elems = []
    corners_multiple = 1
    for th in tile_hashes:
        found_elems = []
        found_elems_ix = []
        for i in range(4):
            if borders.count(th[1][i]) > th[1].count(th[1][i]):
                found_elems.append(th[1][i])
                found_elems_ix.append(i)
        if len(found_elems) == 2:
            corners.append((th[0], th[1][0:4]))
            corners_found_elems.append(found_elems_ix)
            corners_multiple *= int(th[0])
    if part == 1:
        return corners_multiple

    image = get_image(tiles, tile_hashes, corners, corners_found_elems)

    hash_numbers = 0
    for row in image:
        hash_numbers += np.count_nonzero(row == '#')

    for i in range(8):
        if i == 4:
            image = np.flip(image, 1)

        image = np.rot90(image, 1)
        monsters = check_for_monsters(image)
        if monsters > 0:
            return hash_numbers - monsters * monster.count('#')

    return -1