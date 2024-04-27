class Solution:
    def countPairs(self, deli: List[int]) -> int:
            powers = set([2**i for i in range(0, 22)])
            freq = Counter(deli)
            ans = 0
            done = {}
            for d in freq.keys():
                for p in powers:
                    if (p - d) in freq and (d, p - d) not in done:
                        done[(p-d, d)] = True
                        count1 = freq[p-d]
                        count2 = freq[d]
                        # print(d, p-d, p, count1, count2, ans)
                        ans += (count1 * count2 if d != p - d else (count1 * (count1 - 1)) // 2) % (10**9 + 7)
            return ans 