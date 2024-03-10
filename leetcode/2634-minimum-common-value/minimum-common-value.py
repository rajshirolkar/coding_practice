class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = set(nums1)
        s2 = set(nums2)
        return min(s1.intersection(s2)) if s1.intersection(s2) else -1