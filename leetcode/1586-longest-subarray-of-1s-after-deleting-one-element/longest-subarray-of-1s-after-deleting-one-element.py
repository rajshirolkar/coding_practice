class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        curr_len = prev_len = max_len = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                max_len = max(max_len, curr_len + prev_len)
                prev_len = curr_len
                curr_len = 0
            else:
                curr_len += 1
        if curr_len == len(nums):
            return curr_len - 1
        return max(max_len, curr_len + prev_len)

            # INnovative
            # # 1 1 0 1 1 1 0 1 1 1
            # s = ''.join([str(i) for i in nums])
            # new_nums = s.split('0')
            # # print(new_nums)
            # if len(new_nums) == 1:
            #     return len(new_nums[0]) - 1
            # max_count = 0
            # for i in range(len(new_nums) - 1):
            #     max_count = max(max_count, len(new_nums[i]) + len(new_nums[i+1]))
            # return max_count
        