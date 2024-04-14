class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num-1] < 0:
                res.append(num)
            else:
                nums[num-1] *= -1
        return res
