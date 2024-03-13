class Solution:
    def pivotInteger(self, n: int) -> int:
        sumn = (n*(n+1))//2
        prev = 0
        sum1 = 0
        for i in range(1,n+1):
            sum1 += i
            # sum2 = sumn - ((i-1)*i//2)
            sum2 = sumn - prev
            prev = sum1
            if sum1 == sum2:
                return i

        return -1