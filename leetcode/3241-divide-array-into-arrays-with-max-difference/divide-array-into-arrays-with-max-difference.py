class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        i = 0
        while i < len(nums)-2:
            if nums[i+2] - nums[i] > k:
                return []
            else:
                ans.append([nums[i], nums[i+1], nums[i+2]])
            i += 3
        return ans