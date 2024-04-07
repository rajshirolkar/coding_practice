class Solution:
    def checkValidString(self, s: str) -> bool:
        cnt = 0
        for c in s:
            if c in "(*":
                cnt += 1
            elif cnt:
                cnt -= 1
            else:
                return False
        cnt = 0
        for c in s[::-1]:
            if c in "*)":
                cnt += 1
            elif cnt:
                cnt -= 1
            else:
                return False
        return True
        
        
        