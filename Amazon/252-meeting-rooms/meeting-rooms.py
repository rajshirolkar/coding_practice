class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        new_interval = sorted(intervals, key=lambda x:x[0])

        for i in range(1,len(new_interval)):
            start0, end0 = new_interval[i-1]
            start1, end1 = new_interval[i]
            if start1 < end0:
                return False
        return True
