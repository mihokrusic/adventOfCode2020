def get_trees(input, move_x, move_y):
    h = len(input)
    w = len(input[0].rstrip())

    curr_x = 0
    curr_y = 0
    trees = 0
    while (curr_y < h):
        trees += int(input[curr_y][curr_x] == '#')

        curr_x = (curr_x + move_x) % w
        curr_y += move_y

    return trees

def part1(input):
    return get_trees(input, 3, 1)


def part2(input):
    solution = 1
    solution *= get_trees(input, 1, 1)
    solution *= get_trees(input, 3, 1)
    solution *= get_trees(input, 5, 1)
    solution *= get_trees(input, 7, 1)
    solution *= get_trees(input, 1, 2)
    return solution