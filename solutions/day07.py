import re

def __parse_input(input):
    parsed = list()
    for line in input:
        temp = re.match(r"(.*) bags contain (.*)", line.rstrip()).groups()
        contains_temp = temp[1][:-1].split(', ')
        contains = list()
        for el in contains_temp:
            el_match = re.match(r"(\d*) (.*) bags?", el)
            contains.append(None if el_match == None else el_match.groups())

        parsed.append([temp[0], contains])

    return parsed

def part1(input):
    parsed = __parse_input(input)

    bags = ['shiny gold']
    current_ix = 0
    while current_ix < len(bags):
        for el in parsed:
            for el_contains in el[1]:
                if el_contains == None:
                    continue

                if (el_contains[1] == bags[current_ix]):
                    bags.append(el[0])

        current_ix += 1

    return len(set(bags)) - 1

def part2(input):
    parsed = __parse_input(input)

    bags = [('shiny gold', 1)]
    current_bags = 0

    ix = 0
    while len(bags) > 0:
        child_bags = []
        line = parsed[ix]
        if line[0] == bags[0][0]:
            for contain_el in line[1]:
                if contain_el != None:
                    child_bags.append((contain_el[1], int(contain_el[0]) * int(bags[0][1])))
            bags.extend(child_bags)
            popped_bag = bags.pop(0)
            current_bags += popped_bag[1]
            ix = 0
        else:
            ix += 1

    return current_bags - 1