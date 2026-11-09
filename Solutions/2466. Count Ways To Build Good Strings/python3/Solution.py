import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.countGoodStrings(3,3,1,1))
    print(time.time() - start)

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        result = 0
        mod = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        for i in range(min(zero, one), high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % mod
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % mod

        for i in range(low, high + 1):
            result = (result + dp[i]) % mod
        return result

if __name__ == '__main__':
    sys.exit(main())