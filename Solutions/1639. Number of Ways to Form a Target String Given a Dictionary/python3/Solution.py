from collections import defaultdict
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.numWays(["acca","bbbb","caca"], "aba"))
    print(time.time() - start)

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

if __name__ == '__main__':
    sys.exit(main())