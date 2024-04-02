class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        sc = set(s)
        tc = set(t)
        if len(sc) != len(tc):
            return False
        
        for i in range(len(s)):
            val = d.get(s[i], -1)
            if val == -1:
                d[s[i]] = t[i]
            elif val != t[i]:
                return False
        return True