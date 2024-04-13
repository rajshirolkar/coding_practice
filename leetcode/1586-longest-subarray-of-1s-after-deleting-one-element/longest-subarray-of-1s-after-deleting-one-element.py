class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
            # 1 1 0 1 1 1 0 1 1 1
            s = ''.join([str(i) for i in nums])
            new_nums = s.split('0')
            # print(new_nums)
            if len(new_nums) == 1:
                return len(new_nums[0]) - 1
            max_count = 0
            for i in range(len(new_nums) - 1):
                max_count = max(max_count, len(new_nums[i]) + len(new_nums[i+1]))
            return max_count
        