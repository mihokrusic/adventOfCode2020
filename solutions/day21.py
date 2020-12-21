def parse_input(input):
    foods = []
    for line in input.split('\n'):
        tokens = line.split(' (contains ')
        ingredients = set(tokens[0].split(' '))
        allergens = set(tokens[1].replace(')', '').split(', '))
        foods.append((ingredients, allergens))
    return foods

def solve(input, part):
    foods = parse_input(input)

    ingredients_count = dict()
    possible = dict()
    for ingredients, allergens in foods:
        # read about defaultdict
        for ingredient in ingredients:
            if ingredient not in ingredients_count.keys():
                ingredients_count[ingredient] = 1
            else:
                ingredients_count[ingredient] += 1

        for a in allergens:
            if a not in possible:
                possible[a] = ingredients.copy()
            else:
                possible[a] &= ingredients

    all_possible = set()
    for p in possible.values():
        all_possible.update(p)
    without_allergens = list(ingredients_count.keys() - all_possible)

    if part == 1:
        return sum(ingredients_count[x] for x in without_allergens)

    ix = 0
    keys = list(possible.keys())
    solved = []
    while ix < len(keys):
        possible_ingredients = possible[keys[ix]]
        if len(possible_ingredients) > 1:
            possible_ingredients = [x for x in possible_ingredients if x not in solved]
            possible[keys[ix]] = possible_ingredients
        if len(possible_ingredients) == 1 and list(possible_ingredients)[0] not in solved:
            solved.append(list(possible_ingredients)[0])
            ix = 0
            continue

        ix += 1
    sorted_allergens = list(possible.keys())
    sorted_allergens.sort()
    sol = ''
    for sa in sorted_allergens:
        sol += list(possible[sa])[0] + ','
    return sol[:-1]