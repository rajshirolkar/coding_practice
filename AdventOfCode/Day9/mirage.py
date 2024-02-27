def read_file(file_name):
    input_array = []
    with open(file_name, "r") as file:
        for line in file:
            input_array.append(line.strip())
        return input_array


lines = read_file("input.txt")


def get_diff(sequence):
    return [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]


def get_prediction(sequence):
    if len(set(sequence)) == 1:
        return sequence[0]
    else:
        return sequence[-1] + get_prediction(get_diff(sequence))


def part1(lines):
    ans = 0
    for line in lines:
        sequence = list(map(int, line.split()))
        ans += get_prediction(sequence)
    return ans


# print(part1(lines))

def part2(lines):
    ans = 0
    for line in lines:
        sequence = list(map(int, line.split()))
        ans += get_prediction(sequence[::-1])
    return ans


print(part2(lines))
