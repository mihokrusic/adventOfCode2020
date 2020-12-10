import copy
import os

def part1(input):
    adapters = sorted([int(x) for x in input])

    current = 0
    diffs = dict()
    diffs[3] = 1
    for i in adapters:
        diff = i - current
        current = i
        if diff in diffs:
            diffs[diff] += 1
        else:
            diffs[diff] = 1

    return diffs[1] * diffs[3]


def __calculate_chain(adapters, cache, current, target):
    next_adapters = [x for x in adapters if 1 <= x - current <= 3 and x != target]
    sol_here = len([x for x in adapters if 1 <= x - current <= 3 and x == target])
    for el in next_adapters:
        if not el in cache:
            cache[el] = __calculate_chain(adapters, cache, el, target)

        sol_here += cache[el]

    return sol_here

def part2(input):
    adapters = sorted([int(x) for x in input])
    target = adapters[len(adapters) - 1]
    cache = dict()

    solutions = __calculate_chain(adapters, cache, 0, target)
    return solutions