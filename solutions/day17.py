import copy

def __convert_input(input):
    # x-from, x-to, y-from, y-to, z-from, z-to, w-from, w-to
    dims = [-1, len(input) + 1, -1, len(input[0]) + 1, -1, 1, -1, 1]

    # key is x-y-z-w
    cubes = dict()
    for ixr, r in enumerate(input):
        for ixc, c in enumerate(r.rstrip()):
            cubes[__get_key(ixc, ixr, 0, 0)] = c

    return cubes, dims

def __get_key(x, y, z, w):
    return f"{x}-{y}-{z}-{w}"

def __get_active_neighbors(cubes, x, y, z, w):
    active = 0
    for ix in range(x-1, x+2):
        for iy in range(y-1, y+2):
            for iz in range(z-1,z+2):
                for iw in range(w-1,w+2):
                    if ix == x and iy == y and iz == z and iw == w:
                        continue
                    key = __get_key(ix, iy, iz, iw)
                    if key in cubes and cubes[key] == "#":
                        active += 1

    return active

def __get_active_cubes(cubes, dims):
    active = 0
    for ix in range(dims[0], dims[1] + 1):
        for iy in range(dims[2], dims[3] + 1):
            for iz in range(dims[4], dims[5] + 1):
                for iw in range(dims[6], dims[7] + 1):
                    key = __get_key(ix, iy, iz, iw)
                    if key in cubes and cubes[key] == "#":
                        active += 1

    return active

def part1(input):
    cubes, dims = __convert_input(input)

    for _ in range(6):
        new_cubes = copy.deepcopy(cubes)
        for ix in range(dims[0], dims[1] + 1):
            for iy in range(dims[2], dims[3] + 1):
                for iz in range(dims[4], dims[5] + 1):
                    key = __get_key(ix, iy, iz, 0)
                    active_neighbors = __get_active_neighbors(cubes, ix, iy, iz, 0)
                    if key not in cubes or cubes[key] == ".":
                        if active_neighbors == 3:
                            new_cubes[key] = "#"

                    if key in cubes and cubes[key] == "#":
                        if not (2 <= active_neighbors <= 3):
                            new_cubes[key] = "."

        cubes = copy.deepcopy(new_cubes)
        dims[0] -= 1
        dims[1] += 1
        dims[2] -= 1
        dims[3] += 1
        dims[4] -= 1
        dims[5] += 1

    active_cubes = __get_active_cubes(cubes, dims)
    return active_cubes

def part2(input):
    cubes, dims = __convert_input(input)

    for _ in range(6):
        new_cubes = copy.deepcopy(cubes)
        for ix in range(dims[0], dims[1] + 1):
            for iy in range(dims[2], dims[3] + 1):
                for iz in range(dims[4], dims[5] + 1):
                    for iw in range(dims[6], dims[7] + 1):
                        key = __get_key(ix, iy, iz, iw)
                        active_neighbors = __get_active_neighbors(cubes, ix, iy, iz, iw)
                        if key not in cubes or cubes[key] == ".":
                            if active_neighbors == 3:
                                new_cubes[key] = "#"

                        if key in cubes and cubes[key] == "#":
                            if not (2 <= active_neighbors <= 3):
                                new_cubes[key] = "."

        cubes = copy.deepcopy(new_cubes)
        dims[0] -= 1
        dims[1] += 1
        dims[2] -= 1
        dims[3] += 1
        dims[4] -= 1
        dims[5] += 1
        dims[6] -= 1
        dims[7] += 1

    active_cubes = __get_active_cubes(cubes, dims)
    return active_cubes