class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        maxe, mine, N = max(nums), min(nums), len(nums)
        minidx = nums.index(mine)
        maxidx = len(nums)-1
        if N==1:
            return 0
        elif N==2:
            return 1 if nums[0]>nums[1] else 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == maxe:
                maxidx = i
                break
        swaps = minidx + N - maxidx - 1
        if minidx > maxidx:
            swaps -= 1
        return swaps
        