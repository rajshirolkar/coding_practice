class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a1 = abs(ax2 - ax1) * abs(ay2 - ay1)
        a2 = abs(bx2 - bx1) * abs(by2 - by1)

        s1 = min(ax2, bx2) - max(ax1, bx1)
        s2 = min(ay2, by2) - max(ay1, by1)

        overlap_area = max(s1, 0) * max(s2, 0)

        return a1 + a2 - overlap_area
