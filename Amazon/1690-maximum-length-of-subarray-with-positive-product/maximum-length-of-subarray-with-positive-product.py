class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = 1 if nums[0] > 0 else 0
        neg = 1 if nums[0] < 0 else 0
        res = pos

        for n in nums[1:]:
            prev_pos, prev_neg = pos, neg
            if n > 0:
                pos += 1
                neg = prev_neg + 1 if prev_neg > 0 else 0
            elif n < 0:
                neg = prev_pos + 1
                pos = prev_neg + 1 if prev_neg > 0 else 0
            else:
                pos = 0
                neg = 0
            res = max(res,pos)
        return res
