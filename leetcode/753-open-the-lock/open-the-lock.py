class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10) # 9 + 1 = 10 % 10 = 0
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)  # 9-1 = 8 + 10 = 18 % 10 = 8
                res.append(lock[:i] + digit + lock[i+1:])
            return res

        q = deque([("0000", 0)]) # lock, turns
        visit = set(deadends)
        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append((child, turns+1))
        return -1
