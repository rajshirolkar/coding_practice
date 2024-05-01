class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        res = word
        for i, c in enumerate(word):
            if c == ch:
                res = word[:i+1][::-1] + word[i+1:]
                break
        return res