class Solution:
    def racecar(self, target: int) -> int:
        # q = moves, position, speed
        q = deque([(0,0,1)])
        visit = set()

        while q:
            moves, position, speed = q.popleft()

            if position == target:
                return moves
            
            if (position, speed) in visit:
                continue  
            else:
                visit.add((position, speed))

                q.append((moves + 1, position + speed, speed * 2))

                # reverse if we need to go in the opposite direction
                if (position+speed > target and speed > 0) or (position+speed < target and speed < 0):
                    speed = -1 if speed > 0 else 1
                    q.append((moves+1, position, speed))