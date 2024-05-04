class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        last = float('-inf')
        arrow = 0
        for point in points:
            start, end = point
            if start > last:
                arrow += 1
                last = end
        return arrow
        