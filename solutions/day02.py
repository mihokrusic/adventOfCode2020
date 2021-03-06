import re

def __get_parts(line):
    return re.match(r"(\d*)-(\d*) (\w): (\w*)", line).groups()

def part1(input):
    matches = 0

    for line in input:
        (start, end, char, password) = __get_parts(line)
        matches += int((int(start) <= password.count(char) <= int(end)))

    return matches

def part2(input):
    matches = 0

    for line in input:
        (start, end, char, password) = __get_parts(line)
        if (int(password[int(start) - 1] == char) + int(password[int(end) - 1] == char) == 1):
            matches += 1

    return matches