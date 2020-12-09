def __get_parts(preamble_numbers, target):
    for i in range(len(preamble_numbers)):
        for j in range(i + 1, len(preamble_numbers)):
            if (preamble_numbers[i] + preamble_numbers[j] == target and preamble_numbers[i] != preamble_numbers[j]):
                return True

    return False

def part1(input, preamble):
    numbers = [int(x) for x in input]
    ix = preamble
    preamble_numbers = numbers[:ix]

    for i in range(preamble, len(input)):
        if not __get_parts(preamble_numbers, numbers[i]):
            return numbers[i]

        preamble_numbers.pop(0)
        preamble_numbers.append(numbers[i])

    return -1

def part2(input, target):
    numbers = [int(x) for x in input]
    current = 0
    numbers_set = set()
    for i in range(len(numbers)):
        numbers_set.clear()
        numbers_set.add(numbers[i])
        current = numbers[i]
        for j in range(i + 1, len(numbers)):
            numbers_set.add(numbers[j])
            current += numbers[j]

            if current > target:
                break

            if current == target:
                sorted_set = sorted(numbers_set)
                return sorted_set[0] + sorted_set[len(sorted_set) - 1]

    return -1
