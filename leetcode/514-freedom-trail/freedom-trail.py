class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        cache = {}
        def dfs(r,k):
            if k== len(key):
                return 0
            if (r,k) in cache:
                return cache[(r,k)]
            res = float("inf")
            for i, c in enumerate(ring):
                # found the characte
                if c == key[k]:
                    min_dist = min(
                        abs(r-i),
                        len(ring) - abs(r-i)
                    )

                    res = min(
                        res,
                        min_dist + 1 + dfs(i, k+1)
                    )
            cache[(r,k)] = res
            return res
        return dfs(0, 0)
