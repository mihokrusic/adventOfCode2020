from collections import namedtuple

def part1(input):
    target = int(input[0])
    buses = input[1].split(',')

    current = None
    time = None

    for bus in buses:
        if bus == "x":
            continue

        tmp_time = int(bus) - (target % int(bus))
        if (time == None) or (tmp_time < time):
            time = tmp_time
            current = int(bus)

    return time * current

def part2(input):
    buses = input[1].split(',')
    Problem = namedtuple("Problem", "div rem")

    problems = list()
    N = 1
    for el in enumerate(buses):
        if el[1] == 'x':
            continue


        problem = Problem(int(el[1]), (int(el[1]) - el[0]) % int(el[1]))
        problems.append(problem)
        N *= problem.div

    sol = 1
    for problem in problems:
        b = problem.rem
        Ni = int(N / problem.div)

        xi_t = Ni % problem.div
        xi = 1
        while True:
            if (xi * xi_t) % problem.div == 1:
                break
            xi += 1

        sol += (b * Ni * xi)

    return (sol % N) - 1
