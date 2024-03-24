class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        s = set(nums)
        if 0 in s:
            s.remove(0)
        return len(s)
        