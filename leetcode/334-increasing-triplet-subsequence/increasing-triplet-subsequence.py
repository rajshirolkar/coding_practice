class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_small, second_small = float(inf), float(inf)
        for i in range(len(nums)):
            if nums[i] <= first_small:
                first_small = nums[i]
            elif nums[i] <= second_small:
                second_small = nums[i]
            else:
                return True
        return False
