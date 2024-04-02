class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n-1,0,-1):
            temp = [0] * i
            for j in range(len(temp)):
                temp[j] = (nums[j] + nums[j+1]) % 10
            nums = temp
        
        return nums[0]