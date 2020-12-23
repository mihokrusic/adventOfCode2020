class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def get_chain(start_at, dt, delimiter = ''):
    head = dt[start_at]
    next = head.next
    chain = ''
    while next.value != 1:
        chain += f'{str(next.value)}{delimiter}'
        next = next.next
    return chain

def get_destination_value(current, lowest, highest, picked):
    destination = current.value - 1
    while True:
        if destination == current.value:
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

    head = None
    curr = None

    dt = dict()

    for el in cups:
        if head == None:
            head = Node(el)
            curr = head
        else:
            curr.next = Node(el)
            curr = curr.next

        dt[el] = curr
    curr.next = head
    current = head
    loop = 0
    while loop < cnt:
        following_1_node = current.next
        following_2_node = following_1_node.next
        following_3_node = following_2_node.next
        picked = [following_1_node.value, following_2_node.value, following_3_node.value]
        destination_value = get_destination_value(current, lowest, highest, picked)

        destination_node = dt[destination_value]

        current.next = following_3_node.next
        following_3_node.next = destination_node.next
        destination_node.next = following_1_node

        current = current.next
        loop += 1
    return dt

def solve(input, part):
    cups = list(map(int, list(input)))

    if part == 1:
        dt = iterate(cups, 100)
        return get_chain(1, dt)
    else:
        highest = max(cups)
        for _ in range(1000000 - len(cups)):
            cups.append(highest + 1)
            highest += 1
        dt = iterate(cups, 10000000)
        return dt[1].next.value * dt[1].next.next.value