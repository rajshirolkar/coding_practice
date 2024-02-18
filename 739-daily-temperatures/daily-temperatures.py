class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        waiting_days = [0]*len(temps)
        for i in range(len(temps)):
            if len(stack) == 0:
                stack.append((temps[i], i))
            else:
                while stack and stack[-1][0] < temps[i]:
                    x, y = stack.pop()
                    waiting_days[y] = i - y
                stack.append((temps[i], i))
        return waiting_days

