x = "3+2*2"


def calculate(s):
    cur = prev = res = 0
    sign = "+"
    for i in range(len(s)):
        if s[i].isdigit():
            cur = cur * 10 + int(s[i])
        if s[i] in "+-*/" or i == len(s) - 1:
            if sign == "+":
                res += prev
                prev = cur
            elif sign == "-":
                res += prev
                prev = -cur
            elif sign == "*":
                prev *= cur
            elif sign == "/":
                prev /= cur
            sign = s[i]
            cur = 0
    res += prev
    return res


print(calculate(x))
