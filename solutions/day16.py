import re

def __get_input(input):
    rules = list()
    me = list()
    others = list()

    checking_part = 1
    for line in input:
        if len(line.rstrip()) == 0:
            checking_part += 1
            continue
        if re.match(r"(your ticket|nearby ticket)", line) != None:
            continue

        if checking_part == 1:
            line_grps = re.match(r"([\w\- ]+): (\d+)-(\d+) or (\d+)-(\d+)", line).groups()
            rules.append((line_grps[0], int(line_grps[1]), int(line_grps[2]), int(line_grps[3]), int(line_grps[4])))
            pass
        if checking_part == 2:
            me = [int(x) for x in line.rstrip().split(',')]
            pass
        if checking_part == 3:
            others.append([int(x) for x in line.rstrip().split(',')])
            pass

    return rules, me, others

def part1(input):
    rules, me, others = __get_input(input)

    scanning_error_rate = 0
    for other in others:
        for v in other:
            found = False
            for rule in rules:
                if rule[1] <= v <= rule[2] or rule[3] <= v <= rule[4]:
                    found = True

            if (not found):
                scanning_error_rate += v

    return scanning_error_rate

def part2(input):
    rules, me, others = __get_input(input)
    invalid_others = list()
    for ix, other in enumerate(others):
        for v in other:
            found = False
            for rule in rules:
                if rule[1] <= v <= rule[2] or rule[3] <= v <= rule[4]:
                    found = True

            if (not found):
                invalid_others.append(ix)

    for ix in reversed(invalid_others):
        del others[ix]

    valid_fields = []
    for i in range(len(others[0])):
        valid_fields.append([])
        for rule in rules:
            valid = True
            for other in others:
                if not (rule[1] <= other[i] <= rule[2] or rule[3] <= other[i] <= rule[4]):
                    valid = False
                    break

            if valid:
                valid_fields[-1].append(rule[0])

    found_fields = []
    while True:
        ix = 0
        found = False
        while ix < len(valid_fields):
            if len(valid_fields[ix]) != 1:
                valid_fields[ix] = [x for x in valid_fields[ix] if not x in found_fields]
            if len(valid_fields[ix]) == 1 and not valid_fields[ix][0] in found_fields:
                found_fields.append(*valid_fields[ix])
                found = True
                ix = 0
            ix += 1
        if not found:
            break

    result = 1
    for ix, v in enumerate(valid_fields):
        if "departure" in v[0]:
            result *= me[ix]
    return result