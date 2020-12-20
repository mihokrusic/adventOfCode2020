import re
import itertools

def __get_rules(lines_to_parse):
    rules = dict()
    to_parse = dict()
    for line in lines_to_parse:
        constant = re.match(r'^(\d+): "(\w+)"', line)
        if constant != None:
            rule_id, value = constant.groups()
            rules[int(rule_id)] = f'{value}'
            continue

        complex = re.match(r'^(\d+): (.*)', line)
        if complex != None:
            rule_id, values = complex.groups()
            to_parse[int(rule_id)] = [list(map(int, x.split(' '))) for x in values.split(' | ')]

    return __calc_rules(rules, to_parse, 0, 1)

def __calc_rules(rules, to_parse, rule_id, level):
    source = to_parse[rule_id]
    allowed = ''
    for part in source:
        current = ''
        for child_rule in part:
            if child_rule in rules:
                current += f'{rules[child_rule]}'
            else:
                if level < 50:
                    rules = __calc_rules(rules, to_parse, child_rule, level + 1)
                    current += f'({rules[child_rule]})'
        if allowed != '':
            allowed += '|' + current
        else:
            allowed = current

    rules[rule_id] = f'({allowed})'
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

    # print('\n\n')
    # for key in rules:
    #     print(key, rules[key])
    # print('\n\n')

    # check
    pattern = re.compile(r'^' + rules[0] + '$')
    matches = 0
    for line in lines_to_check:
        if pattern.match(line) != None:
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