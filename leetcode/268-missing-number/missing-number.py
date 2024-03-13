class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        nsum = (N * (N+1))//2
        for i in nums:
            nsum -= i
        return nsum