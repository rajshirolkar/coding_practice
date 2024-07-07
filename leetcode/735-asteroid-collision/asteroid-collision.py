class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        stack = []

        for a in ast:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                # if incoming asteroid(a) wins
                if diff < 0:
                    stack.pop()
                # if current asteroid wins
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            # if incoming asteroid has won
            if a:
                stack.append(a)
        return stack