import re

class ParsedBag:
    def __init__(self, bag_type, contains):
        self.bag_type = bag_type
        self.contains = None if len(contains) == 1 and contains[0] == None else contains

class Bag:
    def __init__(self, bag_type, amount):
        self.bag_type = bag_type
        self.amount = amount

def __parse_input(input):
    parsed = list()
    for line in input:
        line_grp = re.match(r"(.*) bags contain (.*)", line.rstrip()).groups()
        contains_temp = line_grp[1][:-1].split(', ')
        contains = list()
        for el in contains_temp:
            el_match = re.match(r"(\d*) (.*) bags?", el)
            contains.append(None if el_match == None else el_match.groups())

        parsed.append(ParsedBag(line_grp[0], contains))

    return parsed

def part1(input):
    parsed = __parse_input(input)

    bags = ['shiny gold']
    current_ix = 0
    while current_ix < len(bags):
        for el in parsed:
            if el.contains == None:
                continue

            for el_contains in el.contains:
                if (el_contains[1] == bags[current_ix]):
                    bags.append(el.bag_type)

        current_ix += 1

    return len(set(bags)) - 1

def part2(input):
    parsed = __parse_input(input)

    bags = [Bag('shiny gold', 1)]
    current_bags = 0

    ix = 0
    while len(bags) > 0:
        child_bags = []
        current = parsed[ix]
        if current.bag_type == bags[0].bag_type:
            if current.contains != None:
                for contain_el in current.contains:
                    child_bags.append(Bag(contain_el[1], int(contain_el[0]) * int(bags[0].amount)))

            bags.extend(child_bags)
            popped_bag = bags.pop(0)
            current_bags += popped_bag.amount
            ix = 0
        else:
            ix += 1

    return current_bags - 1