class Solution:
    def minimumKeypresses(self, s: str) -> int:
        sc = Counter(s)
        sc = dict(sorted(sc.items(), key = lambda x:x[1], reverse=True))
        clicks = 0
        offset = 1
        i = 0
        for k in sc.keys():
            clicks += sc[k] * offset
            i += 1
            if i % 9 == 0:
                offset += 1
        return clicks