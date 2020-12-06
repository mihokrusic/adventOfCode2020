def part1(input):
    result = 0
    answers = set()
    for line in input:
        if len(line.rstrip()) == 0:
            result += len(answers)
            answers.clear()

        for c in line.rstrip():
            answers.add(c)

    result += len(answers)
    return result


def part2(input):
    result = 0
    answers = dict()
    group_cnt = 0

    for line in input:
        if len(line.rstrip()) == 0:
            result += len(list(filter(lambda s: s == group_cnt, answers.values())))
            group_cnt = 0
            answers.clear()
            continue

        group_cnt += 1
        for c in line.rstrip():
            if c in answers:
                answers[c] += 1
            else:
                answers[c] = 1

    result += len(list(filter(lambda s: s == group_cnt, answers.values())))

    return result