import re
import itertools

def __get_rules(lines_to_parse):
    rules = dict()
    to_parse = dict()
    for line in lines_to_parse:
        constant = re.match(r'^(\d+): "(\w+)"', line)
        if constant != None:
            rule_id, value = constant.groups()
            rules[int(rule_id)] = set([value])
            continue

        complex = re.match(r'^(\d+): (.*)', line)
        if complex != None:
            rule_id, values = complex.groups()
            to_parse[int(rule_id)] = [list(map(int, x.split(' '))) for x in values.split(' | ')]

    return __calc_rules(rules, to_parse, 0, 1)

def __calc_rules(rules, to_parse, rule_id, level):
    def add_to_current(current, child_rule):
        if len(current) == 0:
            current.extend(list(child_rule))
        else:
            current = [''.join(el) for el in itertools.product(*[current, list(child_rule)])]
        return current

    source = to_parse[rule_id]
    allowed = set()
    for part in source:
        current = list()
        for child_rule in part:
            if child_rule in rules:
                current = add_to_current(current, rules[child_rule])
            else:
                # print(rule_id, child_rule, level, current, allowed)
                rules = __calc_rules(rules, to_parse, child_rule, level + 1)
                current = add_to_current(current, rules[child_rule])

        allowed.update(current)
    rules[rule_id] = allowed
    return rules

def part1(input):
    lines_to_parse = list()
    lines_to_check = list()
    for line in input:
        if re.match(r'^\d', line) != None:
            lines_to_parse.append(line.rstrip())
        if re.match(r'^[a|b]', line) != None:
            lines_to_check.append(line.rstrip())

    # parse
    rules = __get_rules(lines_to_parse)

    # check
    matches = 0
    for line in lines_to_check:
        if line in rules[0]:
            matches += 1
    return matches

def part2(input):
    lines_to_parse = list()
    lines_to_check = list()
    for line in input:
        if re.match(r'^\d', line) != None:
            complex = re.match(r'^(\d+): (.*)', line)
            if complex:
                rule_id, _ = complex.groups()
                if int(rule_id) == 8:
                    lines_to_parse.append('8: 42 | 42 8')
                elif int(rule_id) == 11:
                    lines_to_parse.append('11: 42 31 | 42 11 31')
                else:
                    lines_to_parse.append(line.rstrip())
            else:
                lines_to_parse.append(line.rstrip())
        if re.match(r'^[a|b]', line) != None:
            lines_to_check.append(line.rstrip())

    # parse
    rules = __get_rules(lines_to_parse)

    # check
    matches = 0
    for line in lines_to_check:
        if line in rules[0]:
            matches += 1
    return matches