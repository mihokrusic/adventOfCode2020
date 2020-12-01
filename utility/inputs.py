def read(fileName):
    input = []
    with open("inputs/" + fileName, "r") as infile:
        for line in infile:
            input.append(line)
    return input