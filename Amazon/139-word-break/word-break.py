class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # CF Soln
        q = deque([s])
        visited = set()
        while q:
            word = q.popleft()
            if word in visited:
                continue
            else:
                if not word:
                    return True
                visited.add(word)

                for start_word in wordDict:
                    if word.startswith(start_word):
                        q.append(word[len(start_word):])
        return False
            
        # Neet Code Solution        
        # n = len(s)
        # words = set(wordDict)
        # dp = [False] * (n+1)
        # dp[0] = True

        # for i in range(1,n+1):
        #     for j in range(i):
        #         if dp[j] and s[j:i] in words:
        #             dp[i] = True
        #             break
        # return dp[-1]
        
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
