def get_destination(current, lowest, highest, picked):
    destination = current - 1
    while True:
        if destination == current:
            destination -= 1
        if destination < lowest:
            destination = highest
        if destination not in picked:
            break
        destination -= 1
    return destination

def iterate(cups, cnt):
    lowest = min(cups)
    highest = max(cups)
    loop = 0
    next = cups[0]
    while loop < cnt:
        ix = cups.index(next)
        current = next
        destination = current - 1

        picked = cups[ix + 1:ix + 4]

        cups[ix + 1:ix + 4] = []
        if len(picked) < 3:
            old_len = len(picked)
            picked.extend(cups[0:3-len(picked)])
            cups = cups[3 - old_len:]

        if ix < len(cups) - 1:
            next = cups[ix + 1]
        else:
            next = cups[0]

        destination = get_destination(current, lowest, highest, picked)
        destination_ix = cups.index(destination)
        cups[destination_ix + 1:destination_ix + 1] = picked

        if destination_ix < ix:
            ix += 3
        ix += 1
        if (ix == len(cups)):
            ix = 0
        loop += 1

        if loop % 10000 == 0:
            print(loop)

    return cups

def solve(input, part):
    cups = list(map(int, list(input)))

    if part == 1:
        cups = iterate(cups, 100)
        cups = cups[cups.index(1) + 1:] + cups[:cups.index(1)]
        return ''.join([str(c) for c in cups])
    else:
        highest = max(cups)
        for i in range(1000000 - len(cups)):
            cups.append(highest + 1)
            highest += 1
        cups = iterate(cups, 2000)
        # ix_1 = cups.index(1)
        # before = cups[ix_1 - 1] if ix_1 > 0 else cups[len(cups) - 1]
        # after = cups[ix_1 + 1] if ix_1 < len(cups) - 1 else cups[0]
        # return before * after
        return 2

if __name__ == '__main__':
    solve('916438275', 2)