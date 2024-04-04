class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        ans = []
        s,e = intervals[0]
        for i in range(1, len(intervals)):
            s1, e1 = intervals[i]

            if s1 <= e:
                e = max(e,e1)
                continue
            else:
                ans.append([s,e])
                s,e = s1, e1
        ans.append([s,e])
        return ans