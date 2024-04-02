class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        mxleft, mxright = height[l], height[r]
        water = 0
        while l < r:
            if height[l] <= height[r]:
                l += 1
                mxleft = max(mxleft, height[l])
                water += mxleft - height[l]
            else:
                r -= 1
                mxright = max(mxright, height[r])
                water += mxright - height[r]
        return water