import math


def read_file(file_name):
    input_array = []
    with open(file_name, "r") as file:
        for line in file:
            input_array.append(line.strip())
        return input_array


lines = read_file("input.txt")

maps = {}
path = lines[0]
for line in range(2, len(lines)):
    src, dst = lines[line].split("=")
    maps[src.strip()] = list(i.strip() for i in dst.strip("( )").split(","))


# print(maps)
# print(path)


def part1():
    term = 'AAA'
    p = path[0]
    ptr = 1
    ans = 0

    while term != 'ZZZ':
        if p == 'L':
            term = maps[term][0]
        elif p == 'R':
            term = maps[term][1]
        p = path[ptr]
        ptr += 1
        if ptr == len(path):
            ans += ptr
            ptr = 0
    return ans


# print(part1())


def part2():
    terms = []
    for k, v in maps.items():
        if k[2] == 'A':
            terms.append(k)
    ends = []

    for term in terms:
        p = path[0]
        ptr = 1
        ans = 0
        while term[2] != 'Z':
            if p == 'L':
                term = maps[term][0]
            elif p == 'R':
                term = maps[term][1]
            p = path[ptr]
            ptr += 1
            if ptr == len(path):
                ans += ptr
                ptr = 0
        ends.append(ans)
    return math.lcm(*ends)

print(part2())
