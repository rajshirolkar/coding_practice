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


def getWordNum(line):
    return line.match(numWordsRegex)


def get_last_num(line):
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            return int(line[i])
    return 0


file_read = read_file("input.txt")
res = 0
for line in file_read:
    res += get_first_num(line) * 10 + get_last_num(line)
print(res)
