class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []
        wordSet = set(words)
        memo = {}

        def dfs(word):
            if word in memo:
                return memo[word]
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if ((prefix in wordSet and suffix in wordSet) or 
                    prefix in wordSet and dfs(suffix)):
                    memo[word] = True
                    return True
            memo[word] = False
            return False

        for w in wordSet:
            if dfs(w):
                res.append(w)
        return res