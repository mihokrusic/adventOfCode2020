def __calculate(input, upper_bound):
    numbers = [int(x) for x in input[0].split(',')]
    cache = dict()
    for ix, n in enumerate(numbers):
        cache[n] = ix

    ix = len(numbers) - 1
    diff = 0
    last = numbers[-1]
    while ix < upper_bound - 1:
        if last in cache:
            diff = ix - cache[last]
            cache[last] = ix
        else:
            diff = 0
            cache[last] = ix

        last = diff
        ix += 1
    return last

def part1(input):
    return __calculate(input, 2020)

def part2(input):
    return __calculate(input, 30000000)