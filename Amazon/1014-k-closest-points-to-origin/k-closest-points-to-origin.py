class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        stup = []
        for x,y in points:
            ans = x**2 + y**2
            stup.append((ans,x,y))
        stup.sort()
        res = []
        for i in range(k):
            a,x,y = stup[i]
            res.append([x,y])
        return res