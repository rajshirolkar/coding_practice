class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        area = 0

        while l < r:
            if (r-l)*min(nums[l], nums[r]) > area:
                area = (r-l)*min(nums[l], nums[r])
            else:
                if nums[l] < nums[r]:
                    l += 1
                else:
                    r -= 1
        return area