class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        sc = Counter(s)
        zcnt = ''.join('0' * sc['0'])
        ocnt = ''.join('1' * (sc['1']-1))
        tmpo = ''.join(ocnt)
        tmpz = ''.join(zcnt)
        res = tmpo + tmpz + '1'
        return res