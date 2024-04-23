class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        d = len(nums) - k
        while d>0:
            heapq.heappop(nums)
            d -= 1
        return nums[0]