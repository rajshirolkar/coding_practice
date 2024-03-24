class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse=True, key=lambda a:a[1])
        res = 0
        for box, units in boxTypes:
            if truckSize >= box:
                truckSize -= box
                res += box*units
            else:
                res += truckSize * units
                break
        return res
