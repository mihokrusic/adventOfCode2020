import re

def __get_parts(line):
    return re.match(r"(\d*)-(\d*) (\w): (\w*)", line).groups()

def part1(input):
    matches = 0

    for line in input:
        (start, end, char, password) = __get_parts(line)

        count = password.count(char)
        if (count >= int(start) and count <= int(end)):
            matches += 1

    return matches

def part2(input):
    matches = 0

    for line in input:
        (start, end, char, password) = __get_parts(line)

        start_match = password[int(start) - 1] == char
        end_match = password[int(end) - 1] == char
        if (start_match or end_match) and not (start_match and end_match):
            matches += 1

    return matches