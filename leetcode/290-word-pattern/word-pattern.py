class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hmap = {}
        slist = s.split(" ")
        vis = set()
        if len(pattern) != len(slist):
            return False

        for i, p in enumerate(pattern):
            if p not in hmap:
                if slist[i] not in vis:
                    hmap[p] = slist[i]
                    vis.add(slist[i])
                else:
                    return False
            else:
                if hmap[p] != slist[i]:
                    return False
        return True
        