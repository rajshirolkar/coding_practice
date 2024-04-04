class Solution:
    def maxDepth(self, s: str) -> int:
        maxdepth = 0
        curdepth = 0
        for i in s:
            if i == '(':
                curdepth += 1
                maxdepth = max(maxdepth, curdepth)
            elif i == ')':
                curdepth -= 1
        return maxdepth