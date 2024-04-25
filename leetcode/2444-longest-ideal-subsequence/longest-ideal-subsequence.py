class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for c in s:
            curr = ord(c) - ord('a') # 0-indexed values
            longest = 1
            for prev in range(26):
                if abs(curr - prev) <= k:
                    longest = max(longest, 1 + dp[prev])
            dp[curr] = longest
        return max(dp)
        
        
        
        n = len(s)
        dp = {}
        def dfs(subseq,i):
            if i == n:
                return len(subseq)
            if i in dp:
                return dp[i]
            
            if (not subseq) or (abs(ord(s[i]) - ord(subseq[-1])) <= k):
                dp[i] = max(dfs(subseq, i+1), dfs(subseq+s[i], i+1))
                return dp[i]
            else:
                dp[i] = dfs(subseq, i+1)
                return dp[i]
        return dfs("", 0)
