class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one, two = 0, 0, 0
        for n in nums:
            if n==0:
                zero += 1
            elif n == 1: 
                one += 1
            elif n == 2:
                two += 1
        
        for i, n in enumerate(nums):
            if i < zero:
                nums[i] = 0
            elif i < zero + one:
                nums[i] = 1
            elif i < zero + one + two:
                nums[i] = 2
        return nums