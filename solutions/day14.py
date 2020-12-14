import re

def part1(input):
    memory = dict()
    mask = ""
    for line in input:
        mask_test = re.match(r"mask = ((?:X|1|0)*)", line.rstrip())
        mem_test = re.match(r"mem\[(\d+)\] = (\d+)", line.rstrip())

        if (mask_test != None):
            mask = mask_test.groups()[0]
            continue

        if mem_test != None:
            mem_instruction = mem_test.groups()
            mem_location = int(mem_instruction[0])
            mem_value = int(mem_instruction[1])
            mem_value_bin = ("0" * (36 - len(format(mem_value, "b")))) + format(mem_value, "b")

            mem_value_final = ""
            for i in range(len(mask)):
                if mask[i] == "X":
                    mem_value_final += mem_value_bin[i]
                else:
                    mem_value_final += mask[i]

            memory[mem_location] = int(mem_value_final, 2)

    return sum(memory.values())

def part2(input):

    memory = dict()
    mask = ""
    for line in input:
        mask_test = re.match(r"mask = ((?:X|1|0)*)", line.rstrip())
        mem_test = re.match(r"mem\[(\d+)\] = (\d+)", line.rstrip())

        if (mask_test != None):
            mask = mask_test.groups()[0]
        else:
            mem_instruction = mem_test.groups()
            mem_location = int(mem_instruction[0])
            mem_location_bin = ("0" * (len(mask) - len(format(mem_location, "b")))) + str(format(mem_location, "b"))
            mem_value = int(mem_instruction[1])

            mem_location_mask = ""
            for i in range(len(mask)):
                if mask[i] == "0":
                    mem_location_mask += mem_location_bin[i]
                else:
                    mem_location_mask += mask[i]
            unknown_cnt = mem_location_mask.count("X")

            memory_addresses = list()
            for i in range(2**unknown_cnt):
                i_bin = format(i, "b")

                ix = 0
                unknown_mask = "0" * (unknown_cnt - len(i_bin)) + i_bin

                target = mem_location_mask
                for j in range(len(target)):
                    if target[j] == "X":
                        target = target[:j] + unknown_mask[ix] + target[j + 1:]
                        ix += 1
                memory_addresses.append(int(target, 2))

            for m in memory_addresses:
                memory[m] = mem_value


    return sum(memory.values())