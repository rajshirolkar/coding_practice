class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        N = len(tokens)
        tokens = sorted(tokens)
        up, dp = 0, N-1
        max_score = 0
        while not up > dp:
            if tokens[up] <= power:
                power -= tokens[up]
                score += 1
                up += 1
                max_score = max(score, max_score)
            elif score > 0:
                power += tokens[dp]
                dp -= 1
                score -= 1
            else:
                break
        return max_score