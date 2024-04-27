class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        aldict = { o:i for i, o in enumerate(order)}
        for i in range(1, len(words)):
            word1, word2 = words[i-1], words[i]
            flag = False
            min_range = min(len(word1), len(word2))
            for j in range(min_range):
                if aldict[word1[j]] > aldict[word2[j]]:
                    return False
                elif aldict[word1[j]] < aldict[word2[j]]:
                    flag = True
                    break
            if not flag and len(word1) > len(word2):
                return False
        return True