class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        NUMS = "123456789"
        min_digits = len(str(low))
        max_digits = len(str(high))
        ans = []
        curr_width = min_digits
        while curr_width <= max_digits:
            # print(curr_width)
            for i in range(0, 10 - curr_width):
                num = int(NUMS[i:i + curr_width])
                if low <= num <= high:
                    ans.append(num)
            curr_width += 1
        return ans