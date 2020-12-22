from copy import deepcopy

def get_starting_decks(input):
    decks = [[], []]
    for ix, player in enumerate(input.split('\n\n')):
        decks[ix].extend(list(map(int, player.split('\n')[1:])))
    return decks

def play_regular_combat(decks):
    while len(decks[0]) > 0 and len(decks[1]) > 0:
        card_0 = decks[0].pop(0)
        card_1 = decks[1].pop(0)

        if card_0 > card_1:
            decks[0].extend([card_0, card_1])
        else:
            decks[1].extend([card_1, card_0])

    return 0 if len(decks[0]) > 0 else 1

def play_recursive_combat(decks):
    game_history = set()

    while True:
        winner = None
        hash = f'{",".join([str(x) for x in decks[0]])}-{",".join([str(x) for x in decks[1]])}'
        if hash in game_history:
            return 0

        game_history.add(hash)

        card_0 = decks[0].pop(0)
        card_1 = decks[1].pop(0)

        if len(decks[0]) >= card_0 and len(decks[1]) >= card_1:
            sub_decks = deepcopy(decks)
            sub_decks[0] = sub_decks[0][0:card_0]
            sub_decks[1] = sub_decks[1][0:card_1]
            winner = play_recursive_combat(sub_decks)
        else:
            winner = 0 if card_0 > card_1 else 1

        if winner == 0:
            decks[0].extend([card_0, card_1])
        else:
            decks[1].extend([card_1, card_0])

        if len(decks[0]) == 0:
            winner = 1
            break
        elif len(decks[1]) == 0:
            winner = 0
            break

    return winner

def get_result(winning_deck):
    result = 0
    for ix, v in enumerate(list(reversed(winning_deck))):
        result += ((ix + 1) * v)
    return result

def solve(input, part):
    decks = get_starting_decks(input)
    winner = None
    if part == 1:
        winner = play_regular_combat(decks)
    if part == 2:
        winner = play_recursive_combat(decks)

    return get_result(decks[winner])