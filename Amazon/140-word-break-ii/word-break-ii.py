class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        def dfs(string):
            if string in memo:
                return memo[string]

            if not string:
                return [""]
            
            local_res = []
            for word in wordDict:
                if string.startswith(word):
                    sub_words = dfs(string[len(word):])

                    for sub_word in sub_words:
                        local_res.append(word + (" " if sub_word else "") + sub_word)
            memo[string] = local_res
            return local_res
        return dfs(s)