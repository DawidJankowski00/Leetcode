import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.mincostTickets([1,4,6,7,8,20], [2,7,15]))
    print(time.time() - start)

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = days[-1]
        dp = [0] * (n+1)
        dy = set(days)
        for i in range(1, n+1):
            if i not in dy:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i - 1] + costs[0], dp[i - 7] + costs[1] if i >= 7 else costs[1], dp[i - 30] + costs[2] if i >= 30 else costs[2])
        return dp[-1]

if __name__ == '__main__':
    sys.exit(main())