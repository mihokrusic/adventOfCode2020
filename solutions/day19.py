import re

def __calc_rules(rules, to_parse, rule_id, level):
    rule = to_parse[rule_id]
    allowed = ''
    for opt in rule:
        current = ''
        for opt_rule in opt:
            if opt_rule in rules:
                current += f'{rules[opt_rule]}'
            else:
                if level < 10:
                    rules = __calc_rules(rules, to_parse, opt_rule, level + 1)
                    current += f'({rules[opt_rule]})'
        if allowed != '':
            allowed += '|' + current
        else:
            allowed = current

    rules[rule_id] = f'({allowed})'
    return rules

def solve(input, part):
    rules, tests = input.split('\n\n')

    rules_dt = dict()
    to_parse = dict()
    for rule in rules.split('\n'):
        rule_id, val = rule.split(': ')
        rule_id = int(rule_id)

        if part == 2:
            if rule_id == 8:
                val = '42 | 42 8'
            if rule_id == 11:
                val = '42 31 | 42 11 31'
        if '"' in val:
            val = val.strip('"')
            rules_dt[rule_id] = f'{val}'
        else:
            to_parse[rule_id] = [list(map(int, x.split(' '))) for x in val.split(' | ')]

    rules_dt = __calc_rules(rules_dt, to_parse, 0, 1)

    pattern = re.compile(r'^' + rules_dt[0] + '$')
    matches = 0
    for test in tests.split('\n'):
        if pattern.match(test) != None:
            matches += 1
    return matches