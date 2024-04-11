class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remain = len(num) - k
        for digit in num:
            # print(stack, digit)
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        # print("final : ", stack)
        res = ''.join(stack[:remain])
        return res.lstrip('0') or '0'