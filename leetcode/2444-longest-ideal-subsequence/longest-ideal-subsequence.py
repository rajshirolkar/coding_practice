class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # DP approach for each character in the alphabet
        dp = [0] * 26
        for c in s:
            curr = ord(c) - ord('a') # 0-indexed values
            longest = 1
            for prev in range(26):
                if abs(curr - prev) <= k:
                    longest = max(longest, 1 + dp[prev])
            dp[curr] = longest
        return max(dp)
        
        # Recursive approach good for interview
        # n = len(s)
        # dp = {}
        # def dfs(prev,i):
        #     if i == n:
        #         return 0
        #     if (prev, i) in dp:
        #         return dp[(prev, i)]
        #     res = dfs(prev, i+1)
        #     if (not prev) or (abs(ord(s[i]) - ord(prev)) <= k):
        #         res = max(res, 1 + dfs(s[i], i+1))
        #     dp[(prev,i)] = res
        #     return res
        # return dfs("", 0)
