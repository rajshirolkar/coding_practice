class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numdict = {i:1 for i in nums}
        print(numdict)
        for i in range(len(nums)+1):
            if i not in numdict:
                return i