class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = {}
        for word in strs:
            sort_word = ''.join(sorted(word))
            if sort_word in ana_map:
                ana_map[sort_word].append(word)
            else:
                ana_map[sort_word] = [word]
        res = []
        for v in ana_map.values():
            res.append(v)
        return res