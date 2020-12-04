import re

def check_if_in_range(value, start, end):
    try:
        return start <= int(value) <= end
    except:
        return False

def has_enough_fields(current):
    if len(current) == 8:
        return True

    if (len(current) == 7 and "cid" not in current):
        return True

    return False

def is_valid(current):
    if (not has_enough_fields(current)):
        return False

    if not check_if_in_range(current['byr'], 1920, 2002):
        return False

    if not check_if_in_range(current['iyr'], 2010, 2020):
        return False

    if not check_if_in_range(current['eyr'], 2020, 2030):
        return False

    hgt = re.match(r"(\d+)(cm|in)", current["hgt"])
    if hgt == None:
        return False

    hgt_values = hgt.groups()
    if hgt_values[1] == 'cm' and not check_if_in_range(hgt_values[0], 150, 193):
        return False
    if hgt_values[1] == 'in' and not check_if_in_range(hgt_values[0], 59, 76):
        return False

    if (re.match(r"^#[abcdef0-9]{6}$", current["hcl"]) == None):
        return False

    if (re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", current["ecl"]) == None):
        return False

    if (re.match(r"^\d{9}$", current["pid"]) == None):
        return False

    return True

def part1(input):
    valid = 0
    current = dict()
    for line in input:
        if len(line.rstrip()) != 0:
            parts = re.findall(r"\b([A-Za-z0-9:#]+)\b", line.lower())
            for part in parts:
                values = re.match(r"([A-Za-z0-9#]+):([A-Za-z0-9#])", part).groups()
                current[values[0]] = values[1]

        else:
            valid += int(has_enough_fields(current))
            current.clear()
            pass

    valid += int(has_enough_fields(current))
    return valid


def part2(input):
    valid = 0
    current = dict()
    for line in input:
        if len(line.rstrip()) != 0:
            parts = re.findall(r"\b([A-Za-z0-9:#]+)\b", line)
            for part in parts:
                values = re.match(r"([A-Za-z0-9#]+):([A-Za-z0-9#]+)", part).groups()
                current[values[0]] = values[1]

        else:
            valid += int(is_valid(current))
            current.clear()
            pass

    valid += int(is_valid(current))
    return valid