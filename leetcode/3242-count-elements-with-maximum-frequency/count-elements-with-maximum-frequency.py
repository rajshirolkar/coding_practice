class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nc = Counter(nums)
        maxnc = max(nc.values())
        res = 0
        for ele in nc:
            if nc[ele] == maxnc:
                res += nc[ele]
        return res