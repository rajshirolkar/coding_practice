class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        res = ""
        l1, l2 = len(word1), len(word2)
        while i < l1 and i<l2:
            res += word1[i] + word2[i]
            i += 1
        
        if l1 > l2:
            res += word1[i:]
        elif l1<l2:
            res += word2[i:]
        return res
        
        