class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        maxNum = -1
        maxDict = defaultdict(int)
        nums = set(nums)
        for n in nums:
            maxDict[abs(n)] += 1
        
        for k,v in maxDict.items():
            if k > maxNum and v == 2:
                maxNum = k
        return maxNum