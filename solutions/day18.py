import copy

class Node:
    def __init__(self, left, right, operator, depth):
        self.left = left
        self.right = right
        self.operator = operator
        self.depth = depth

    def __repr__(self):
        return f'operator: {self.operator}, left: {self.left}, right: {self.right}, depth {self.depth}'

def __parse(formula):
    nodes = list()

    depth = 0
    max_depth = 0
    operator = None
    operator_depth = 0
    in_exp = False
    left = None
    for c in formula:
        if c == '+' or c == '*':
            operator = c
            operator_depth = depth
            in_exp = True
        if c == '(':
            depth += 1
            if in_exp:
                nodes.append(Node(left, None, operator, operator_depth))
                left = None
                in_exp = False
        if c == ')':
            depth -= 1
            if in_exp:
                nodes.append(Node(left, None, operator, operator_depth))
                left = None
                in_exp = False
        if c.isnumeric():
            if in_exp:
                nodes.append(Node(left, int(c), operator, operator_depth))
                left = int(c)
                in_exp = False
            else:
                left = int(c)

        if depth > max_depth:
            max_depth = depth

    return nodes, max_depth

def __calc_node(left, right, operator):
    if operator == '*':
        return left * right
    if operator == '+':
        return left + right
    raise Exception('Invalid operator')

def __remove_groups(nodes, max_depth, addition_first = False):
    results = copy.deepcopy(nodes)
    depth_curr = max_depth
    start_ix = None
    result_part = 0
    ix = 0
    while ix < len(results):
        if results[ix].depth == depth_curr:
            if start_ix == None:
                start_ix = ix
        else:
            if start_ix != None:
                if addition_first:
                    result_part = __calc_addition_first(results[start_ix:ix])
                else:
                    result_part = __calc_no_precedence(results[start_ix:ix])
                results[ix].left = result_part
                if (start_ix > 0):
                    results[start_ix - 1].right = result_part
                start_ix = None

        ix += 1

        if (ix == len(results)):
            if start_ix != None:
                if addition_first:
                    result_part = __calc_addition_first(results[start_ix:ix])
                else:
                    result_part = __calc_no_precedence(results[start_ix:ix])
                if (start_ix > 0):
                    results[start_ix - 1].right = result_part
                start_ix = None

            if depth_curr > 0:
                results = [node for node in results if node.depth < depth_curr]
                depth_curr -= 1
                ix = 0
                if depth_curr == 0:
                    break
    return results

def __calc_no_precedence(nodes):
    result = None
    for node in nodes:
        result = __calc_node(result if result != None else node.left, node.right, node.operator)
    return result

def __calc_addition_first(nodes):
    results = copy.deepcopy(nodes)
    start_ix = None
    ix = 0
    result_part = 0
    while (ix < len(results)):
        node = results[ix]

        if node.operator == '+':
            if start_ix == None:
                start_ix = ix
        else:
            if start_ix != None:
                result_part = __calc_no_precedence(results[start_ix:ix])
                results[ix].left = result_part
                if (start_ix > 0):
                    results[start_ix - 1].right = result_part
                del results[start_ix:ix]
                ix = start_ix - 1
                start_ix = None

        ix += 1

        if (ix == len(results)):
            if start_ix != None:
                result_part = __calc_no_precedence(results[start_ix:ix])
                if (start_ix > 0):
                    results[start_ix - 1].right = result_part
                if len(results) != 1:
                    del results[start_ix:ix]
                start_ix = None

    if len(results) == 0:
        return result_part
    else:
        return __calc_no_precedence(results)

def part1(input):
    result = 0
    for line in input:
        formula = line.rstrip().replace(' ', '')
        nodes, max_depth = __parse(formula)
        nodes = __remove_groups(nodes, max_depth)
        formula_result = __calc_no_precedence(nodes)
        result += formula_result
    return result

def part2(input):
    result = 0
    for line in input:
        formula = line.rstrip().replace(' ', '')
        nodes, max_depth = __parse(formula)
        nodes = __remove_groups(nodes, max_depth, True)
        formula_result = __calc_addition_first(nodes)
        result += formula_result

    # print('\n\n')
    return result
