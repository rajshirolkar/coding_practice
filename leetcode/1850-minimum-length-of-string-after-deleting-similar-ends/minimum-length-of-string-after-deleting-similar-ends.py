class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        count = 0
        prev = s[0]
        while l < r:
            if s[l] == s[r]:
                char = s[l]
                while l < len(s) and s[l] == char:
                    l += 1
                    count += 1
                while r > -1 and s[r] == char:
                    r -= 1
                    count += 1
            else:
                return len(s) - count
        return 1 if l == r else 0