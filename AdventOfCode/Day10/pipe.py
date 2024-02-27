def read_file(file_name):
    input_array = []
    with open(file_name, "r") as file:
        for line in file:
            input_array.append(line.strip())
        return input_array


lines = read_file("input.txt")

pipes = {
    '|': (0, 1),
    '-': (1, 0),
    'L': (-1, -1),
    'J': (1, -1),
}
