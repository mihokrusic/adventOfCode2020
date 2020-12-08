import re

def __parse_instruction(instruction, ix, acc):
    ix_new = ix
    acc_new = acc
    if instruction[0] == 'nop':
        ix_new += 1
        pass

    if instruction[0] == 'acc':
        ix_new += 1
        acc_new += int(instruction[1])

    if instruction[0] == 'jmp':
        ix_new += int(instruction[1])

    return (ix_new, acc_new)

def __get_instruction(input, ix):
    ins_grp = re.match(r"([a-z]{3}) ((?:\+|-)\d*)", input[ix].rstrip()).groups()
    return [ins_grp[0], ins_grp[1]]

def part1(input):
    visited_instructions = set()
    ix = 0
    acc = 0

    while ix < len(input):
        if (ix in visited_instructions):
            break

        visited_instructions.add(ix)
        instruction = __get_instruction(input, ix)

        ix, acc = __parse_instruction(instruction, ix, acc)

    return acc

def part2(input):
    visited_instructions = set()
    changed_instructions = set()

    while True:
        visited_instructions.clear()
        ix = 0
        acc = 0
        changed_this_round = False
        while ix < len(input):
            if (ix in visited_instructions):
                break

            visited_instructions.add(ix)
            instruction = __get_instruction(input, ix)
            if (not changed_this_round and not ix in changed_instructions and (instruction[0] == "nop" or instruction[0] == "jmp")):
                changed_this_round = True
                changed_instructions.add(ix)
                instruction[0] = "nop" if instruction[0] == "jmp" else "jmp"

            ix, acc = __parse_instruction(instruction, ix, acc)

        if (ix >= len(input)):
            break

    return acc