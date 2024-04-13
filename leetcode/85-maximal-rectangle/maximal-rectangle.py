class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Solution for largest Rectangle problem
        def largest_rect(heights):
            N = len(heights)
            maxArea = 0
            stack = []
            for i, h in enumerate(heights):
                start = i
                # Pop smaller heights from the stack than current.
                # Calculate their max area each time while popping
                while stack and stack[-1][1] > h:
                    idx, height = stack.pop()
                    maxArea = max(maxArea, height * (i-idx))
                    start = idx
                stack.append((start,h))
            # Calculate max area for each remainng element in stack
            for i,h in stack:
                maxArea = max(maxArea, h * (N - i))
            return maxArea
        
        max_area = 0
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [0] * COLS
        # Solve the largest rect problem for each row
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == '1':
                    dp[c] += 1
                else:
                    dp[c] = 0
            max_area = max(max_area, largest_rect(dp))
        return max_area