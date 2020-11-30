def read(fileName):
    input = []
    with open("inputs/" + fileName + ".txt", "r") as infile:
        for line in infile:
            input.append(line)
    return input