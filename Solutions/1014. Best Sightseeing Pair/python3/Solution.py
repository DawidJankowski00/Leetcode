from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = 0
        score=0
        for i, x in enumerate(values):
            score=max(score, dp+x-i)
            dp=max(dp, x+i)
        return score
