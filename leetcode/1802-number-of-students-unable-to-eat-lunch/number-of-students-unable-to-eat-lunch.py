class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stq = deque(students)
        n = len(sandwiches)
        cnt = 0
        sandwiches.reverse()

        while True:
            if not sandwiches:
                return 0

            if (
                len(set(stq)) == 1 and 
                stq[0] != sandwiches[-1]
            ):
                return n
            
            st_pref = stq.popleft()
            if st_pref == sandwiches[-1]:
                sandwiches.pop()
                n -= 1
            else:
                stq.append(st_pref)
        



