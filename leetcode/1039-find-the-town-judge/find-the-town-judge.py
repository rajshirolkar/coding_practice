class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_a = [0] * (n + 1)
        trust_b = [0] * (n + 1)

        for a,b in trust:
            trust_a[a] += 1
            trust_b[b] += 1
        
        for i in range(1,n+1):
            if trust_a[i] == 0 and trust_b[i] == n-1:
                return i
        return -1