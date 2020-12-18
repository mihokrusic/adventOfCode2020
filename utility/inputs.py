def read(file_name):
    input = []
    with open("inputs/" + file_name, "r") as infile:
        for line in infile:
            input.append(line)
    return input