class Solution:
    def numberOfWays(self, s: str) -> int:
        sc = Counter(s)
        cnt0, cnt1 = sc['0'], sc['1']

        c0, c1 = 0, 0
        ans = 0
        for c in s:
            if c=='0':
                ans += c1*(cnt1-c1)
                c0 += 1
            if c=='1':
                ans += c0*(cnt0-c0)
                c1 += 1
        return ans