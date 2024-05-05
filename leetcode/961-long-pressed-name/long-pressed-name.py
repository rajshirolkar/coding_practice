class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name):
            return False
        i = j = 0
        prev_t = typed[0]
        prev_n = name[0]

        while i < len(typed):
            if prev_t != prev_n:
                return False
        
            ct = cn = 0
            while i < len(typed) and typed[i] == prev_t:
                i += 1
                ct += 1

            while j < len(name) and name[j] == prev_n:
                j += 1
                cn += 1
            if ct < cn:
                return False
            prev_t = typed[i] if i < len(typed) else prev_t
            prev_n = name[j] if j < len(name) else prev_n
        return True if prev_t == prev_n else False