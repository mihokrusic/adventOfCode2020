#!/usr/bin/env python3
import time
import numpy as np
from math import sqrt
from numpy.core.defchararray import title

from numpy.lib.arraysetops import unique

def get_tile_with_hash(hash, tile_hashes, ignore_id):
    for th in tile_hashes:
        if th[0] == ignore_id:
            continue

        if hash in th[1]:
            return th[0]

    return -1

def get_border_hash(tile):
    t = tile[0]
    r = [y[-1] for y in tile]
    b = list(reversed(tile[-1]))
    l = list(reversed([y[0] for y in tile]))

    return [
        int(''.join(t).replace('#', '1').replace('.', '0'),2),
        int(''.join(r).replace('#', '1').replace('.', '0'),2),
        int(''.join(b).replace('#', '1').replace('.', '0'),2),
        int(''.join(l).replace('#', '1').replace('.', '0'),2)
    ]

def get_image(tiles, tile_hashes, corners, corners_found_elems):
    used_sides = dict()
    for th in tile_hashes:
        used_sides[th[0]] = []
        print(th)
    print('\n\n')



    print(corners)
    print(corners_found_elems)


    image_side = int(sqrt(len(tiles.keys())))

    image = [[[] for _ in range(image_side)] for _ in range(image_side)]
    image_ids = [[0 for _ in range(image_side)] for _ in range(image_side)]




    # first (0,0)
    image_ids[0][0] = corners[0][0]
    image[0][0] = np.rot90(np.array(tiles[corners[0][0]]),-1)

    # next (0, 1)
    border_hash = get_border_hash(image[0][0])[1]
    next = get_tile_with_hash(border_hash, tile_hashes, image_ids[0][0])
    print(border_hash, next)

    image_ids[0][1] = next
    image[0][1] = np.rot90(np.array(tiles[next]),-1)

    # next (0, 2)
    border_hash = get_border_hash(image[0][1])[1]
    next = get_tile_with_hash(border_hash, tile_hashes, image_ids[0][1])
    print(border_hash, next)

    image_ids[0][2] = next
    image[0][2] = np.rot90(np.array(tiles[next]),-1)

    # next (1, 0)
    border_hash = get_border_hash(image[0][0])[2]
    next = get_tile_with_hash(border_hash, tile_hashes, image_ids[0][0])
    print(border_hash, next)

    image_ids[1][0] = next
    image[1][0] = np.rot90(np.array(tiles[next]),-1)

    # next (1, 1)
    border_hash = get_border_hash(image[1][0])[1]
    next = get_tile_with_hash(border_hash, tile_hashes, image_ids[1][0])
    print(border_hash, next)

    image_ids[1][1] = next
    image[1][1] = np.rot90(np.array(tiles[next]),-1)

    # next (1, 2)
    border_hash = get_border_hash(image[1][1])[1]
    next = get_tile_with_hash(border_hash, tile_hashes, image_ids[1][1])
    print(border_hash, next)

    image_ids[1][2] = next
    image[1][2] = np.rot90(np.array(tiles[next]),-1)

    # next (3, 0)
    border_hash = get_border_hash(image[1][0])[2]
    next = get_tile_with_hash(border_hash, tile_hashes, image_ids[1][0])
    print(border_hash, next)

    image_ids[2][0] = next
    image[2][0] = np.rot90(np.flip(np.array(tiles[next]),1),1)

    # next (3, 1)
    border_hash = get_border_hash(image[2][0])[1]
    next = get_tile_with_hash(border_hash, tile_hashes, image_ids[2][0])
    print(border_hash, next)

    image_ids[2][1] = next
    image[2][1] = np.rot90(np.array(tiles[next]),2)

    # next (3, 2)
    border_hash = get_border_hash(image[2][1])[1]
    next = get_tile_with_hash(border_hash, tile_hashes, image_ids[2][1])
    print(border_hash, next)

    image_ids[2][2] = next
    image[2][2] = np.rot90(np.array(tiles[next]),1)





    print('\n\n')
    for row in image_ids:
        print(row)
    print('\n\n')

    return image


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

    print('\n\n')
    for row in image:
        s = ''
        for i in range(10):
            s = ''
            for j in range(len(row)):
                s +=  ''.join(row[j][i])
            print(s)
        print('')
    print('\n\n')






if __name__ == '__main__':
    input = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""
    start_time = time.time()
    solve(input, 2)
    print("--- %s seconds ---\n\n" % (time.time() - start_time))