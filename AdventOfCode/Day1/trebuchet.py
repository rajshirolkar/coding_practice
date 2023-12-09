import os
import re

wordsToNum = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

numWordsRegex = r"one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9"
reverseNumWordsRegex = r"eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|1|2|3|4|5|6|7|8|9"


# write a function the takes text input from a file and returns prints the text
def read_file(file_name):
    input_array = []
    # Open the file in read mode
    with open(file_name, "r") as file:
        # Read the contents of the file
        for line in file:
            # Print the current line
            input_array.append(line.strip())
        return input_array


def get_first_num(line):
    for char in line:
        if char.isdigit():
            return int(char)
    return 0


def getFirstandLastNum(line):
    first, last = 0, 0
    x = re.findall(numWordsRegex, line)
    if x[0] in wordsToNum:
        first = wordsToNum[x[0]]
    else:
        first = int(x[0])

    revLine = line[::-1]
    y = re.findall(reverseNumWordsRegex, revLine)

    if y[0] in wordsToNum:
        last = wordsToNum[y[0]]
    else:
        last = int(y[0])
    return first, last


def get_first_num_2(line):
    x = re.findall(numWordsRegex, line)
    if len(x) == 0:
        return 0
    if x[0] in wordsToNum:
        first = wordsToNum[x[0]]
    else:
        first = int(x[0])
    return first


def get_last_num_2(line):
    revLine = line[::-1]
    y = re.findall(reverseNumWordsRegex, revLine)
    if len(y) == 0:
        return 0
    num = y[0][::-1]
    if num in wordsToNum:
        last = wordsToNum[num]
    else:
        last = int(num)
    return last


def get_last_num(line):
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            return int(line[i])
    return 0


file_read = read_file("input2.txt")
res = 0
for line in file_read:
    # res += get_first_num(line) * 10 + get_last_num(line)
    # first, last = getFirstandLastNum(line)
    first = get_first_num_2(line)
    last = get_last_num_2(line)
    print(line, first, last)
    res += first * 10 + last
print(res)


print(get_first_num_2("oneight"))
print(get_last_num_2("oneight"))
