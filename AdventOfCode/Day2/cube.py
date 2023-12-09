def read_file(file_name):
    input_array = []
    with open(file_name, "r") as file:
        for line in file:
            input_array.append(line.strip())
        return input_array


cubeNums = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
res = []
lines = read_file("input.txt")


def partOne(lines):
    for line in lines:
        game = line.split(":")[1]

        gameNo = int(line.split(":")[0].split(" ")[1])

        sets = game.split(";")
        invalid = False
        for set in sets:
            turn = set.split(",")
            # print(turn)
            for t in turn:
                num, color = t.split()
                num = int(num)
                if num > cubeNums[color]:
                    invalid = True
                    break
        if not invalid:
            res.append(gameNo)
    print(sum(res))


def part2(lines):
    for line in lines:
        game = line.split(":")[1]

        gameNo = int(line.split(":")[0].split(" ")[1])

        sets = game.split(";")
        invalid = False
        for set in sets:
            turn = set.split(",")
            # print(turn)
            for t in turn:
                num, color = t.split()
                num = int(num)
                if num > cubeNums[color]:
                    invalid = True
                    break
        if not invalid:
            res.append(gameNo)
    print(sum(res))
