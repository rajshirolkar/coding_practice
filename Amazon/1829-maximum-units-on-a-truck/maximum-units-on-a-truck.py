class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse=True, key=lambda a:a[1])
        res = 0
        for b in boxTypes:
            for i in range(b[0]):
                if truckSize > 0:
                    truckSize -= 1
                    res += b[1]
        return res
