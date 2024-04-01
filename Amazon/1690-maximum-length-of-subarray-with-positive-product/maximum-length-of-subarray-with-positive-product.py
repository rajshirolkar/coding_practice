class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        pos, neg = 0, 0
        if nums[0] > 0: pos = 1
        if nums[0] < 0: neg = 1
        ans = pos
        for i in range(1, n):
            if nums[i] > 0:
                pos = 1 + pos # add to current streak of positive numbers
                neg = 1 + neg if neg > 0 else 0 #add to current streak of negative numbers - unless no streak, then continue 0 streak
            elif nums[i] < 0:
                pos, neg = 1 + neg if neg > 0 else 0, 1 + pos
            else: #when nums[i] == 0
                pos, neg = 0, 0 #dont do anything if you already set it to 0
            ans = max(ans, pos)
        return ans