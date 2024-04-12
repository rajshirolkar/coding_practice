class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxleft, maxright = height[left], height[right]
        water = 0
        while left < right:
            if height[left] <= height[right]:
                left += 1
                maxleft = max(maxleft, height[left])
                water += maxleft - height[left]
            else:
                right -= 1
                maxright = max(maxright, height[right])
                water += maxright - height[right]
        return water