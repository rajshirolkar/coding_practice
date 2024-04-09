class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        l, r = 0, 0
        while r < len(nums):
            # monotonically decreasing queue
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()   
            q.append(r)

            # remove left value from window
            if l > q[0]:
                q.popleft()

            if (r+1) >= k:
                res.append(nums[q[0]])
                l += 1            
            r += 1
        return res