from collections import defaultdict
from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(words[0])
        m = len(target)
        freq = [defaultdict(int) for _ in range(n)]
        for i in range(n):
            for j in range(len(words)):
                freq[i][words[j][i]] += 1
        mod = 10**9 + 7
        dp = [0] * (m+1)
        dp[0] = 1
        for i in range(n):
            for j in range(m-1, -1, -1):
                dp[j+1] += dp[j] * freq[i][target[j]]
                dp[j+1] %= mod
        return dp[m]
