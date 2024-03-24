class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        md = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss in md:
                md[ss].append(s)
            else:
                md[ss] = [s]
        res = []
        for v in md.values():
            res.append(v)
        return res