class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        inc, dec = [0] * n, [0] * n

        for i in range(1,n):
            if security[i] <= security[i-1]:
                inc[i] = inc[i-1] + 1
        for i in range(n-2,0,-1):
            if security[i] <= security[i+1]:
                dec[i] = dec[i+1] + 1
        
        ans = []
        for i in range(time,n-time):
            if inc[i] >= time and dec[i] >= time:
                ans.append(i)
        return ans