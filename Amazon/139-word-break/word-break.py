class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[-1]
        
        # Our Solution        
        # def dfs(cstr, i):
        #     if len(cstr) == cstr.count("*"):
        #         return True
        #     if i>= len(wordDict):
        #         return False
            
        #     if wordDict[i] in cstr:
        #         cstr1 = cstr.replace(wordDict[i], '*')
        #         return dfs(cstr1, i) or dfs(cstr, i+1)
        #     else:
        #         return dfs(cstr,i+1)
        # return dfs(s,0)
