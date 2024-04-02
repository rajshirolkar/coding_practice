class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        maxele = max(damage)
        sumd = sum(damage)
        res = 0
        if maxele >= armor:
            res = sumd - armor
        else:
            res = sumd - maxele
        return res + 1

