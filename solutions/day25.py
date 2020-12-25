MOD = 20201227

def get_loop(public):
    start = 1
    loop = 0
    while True:
        start = (start * 7) % MOD
        loop += 1
        if start == public:
            break
    return loop

def solve(card_public, door_public):
    card_loop = get_loop(card_public)
    door_loop = get_loop(door_public)

    a = 1
    for _ in range(card_loop):
        a = (a * door_public) % MOD

    return a % MOD