def read_file(file_name):
    input_array = []
    with open(file_name, "r") as file:
        for line in file:
            input_array.append(line.strip())
        return input_array


lines = read_file("input.txt")


# Part 1
def part1(lines):
    ans = []
    for line in lines:
        _, cardNum = line.split(":", 1)
        winNums, myNums = cardNum.split("|", 1)
        winNums = winNums.split()
        myNums = myNums.split()
        res = 0
        for num in myNums:
            if num in winNums:
                res += 1
        if res > 0:
            ans.append(2 ** (res - 1))
    print(sum(ans))


def part2(lines):
    ans = []
    cardPoints = {}
    for line in lines:
        cardNum, cards = line.split(":", 1)
        winNums, myNums = cards.split("|", 1)
        winNums = winNums.split()
        myNums = myNums.split()
        res = 0
        for num in myNums:
            if num in winNums:
                res += 1
        cardPoints[int(cardNum.split(" ", 1)[1])] = res
    return cardPoints


cardPoints = part2(lines)

cards = 0
print(cardPoints)


def parttwo(cardPoints, n):
    new_mappings = {n: 1}
    i = n - 1
    while i > 0:
        count = 1
        count += sum(
            [new_mappings[j] for j in range(i + 1, i + cardPoints[i] + 1)]
        )  # 2, 1+4+1
        new_mappings[i] = count
        i -= 1
    print(new_mappings)
    return sum(new_mappings.values())


print(parttwo(cardPoints, len(cardPoints)))
