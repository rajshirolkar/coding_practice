class Solution:
    def minSwaps(self, s: str) -> int:
        N = len(s)

        freq = Counter(s)
        if N%2 == 0:
            if freq['0'] != freq['1']:
                return -1
        else:
            if abs(freq['0']-freq['1']) != 1:
                return -1
        
        if N%2 != 0:
            k = '0' if freq['0'] > freq['1'] else '1'
            cnt = 0
            for i in s:
                if i != k:
                    cnt += 1
                k = '0' if k=='1' else '1'
        else:
            k = '1'
            cnt1 = cnt2 = 0
            for i in s:
                if i != k:
                    cnt1 += 1
                k = '0' if k=='1' else '1'
            k = '0'
            for i in s:
                if i != k:
                    cnt2 += 1
                k = '0' if k=='1' else '1'
            cnt = min(cnt1,cnt2)
        return cnt // 2