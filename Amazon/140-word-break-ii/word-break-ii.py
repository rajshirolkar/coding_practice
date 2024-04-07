class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        trie.build(set(wordDict))
        stack = [(0, [], trie)]
        ans = []
        while stack:
            indx, ls, node = stack.pop()
            if indx == len(s):
                ans.append(ls) 
                continue
            for i in range(indx, len(s)):
                if s[i] not in node.children:
                    break
                node = node.children[s[i]]
                if node.word is not None:
                    stack.append((i + 1, ls + [node.word], trie))
        return [" ".join(items) for items in ans]

class Trie:
    def __init__(self):
        self.children = {}
        self.word = None

    def insert(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()                
            node = node.children[c]
        node.word = word

    def build(self, words):
        for word in words:
            self.insert(word)


        # CF DFS Solution 
        # memo = {}
        # def dfs(string):
        #     if string in memo:
        #         return memo[string]

        #     if not string:
        #         return [""]
            
        #     local_res = []
        #     for word in wordDict:
        #         if string.startswith(word):
        #             sub_words = dfs(string[len(word):])

        #             for sub_word in sub_words:
        #                 local_res.append(word + (" " if sub_word else "") + sub_word)
        #     memo[string] = local_res
        #     return local_res
        # return dfs(s)