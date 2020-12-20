#!/usr/bin/env python3
import time
from copy import copy
import numpy as np
from math import sqrt

from numpy.lib.arraysetops import unique

def __line_hash(tile):
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

def solve(input, part):
    tiles = dict()
    for tile in input.split('\n\n'):
        tile_lines = tile.split('\n')
        tile_id = tile_lines[0].strip('Tile ').strip(':')

        tile = []
        for line in tile_lines[1:]:
            tile.append(list(line.rstrip()))

        tiles[tile_id] = tile

    # side = int(sqrt(len(tiles.keys())))

    borders = []
    tile_hashes = []
    for key in tiles:
        tile = tiles[key]
        normal_hash = __line_hash(tile)

        flip_tile = np.flip(np.array(tile), 1)
        fliped_hash = __line_hash(flip_tile)

        # tile_hashes.append((int(key), [*normal_hash]))
        tile_hashes.append((int(key), [*normal_hash, *fliped_hash]))
        borders.extend(normal_hash)
        borders.extend(fliped_hash)

    for th in tile_hashes:
        print(th)

    corners = 1
    for th in tile_hashes:
        found_elems = 0
        for i in range(4):
            found_elems += 1 if borders.count(th[1][i]) > th[1].count(th[1][i]) else 0
        if found_elems == 2:
            corners *= th[0]

    return corners



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
    solve(input, 1)
    print("--- %s seconds ---\n\n" % (time.time() - start_time))