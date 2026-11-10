class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        costs = [0] + costs
        dp = [inf] * (n + 3)
        dp[n] = costs[n]

        for i in reversed(range(n)):
            dp[i] = costs[i] + min(dp[i+1] + 1, dp[i+2] + 4, dp[i+3] + 9)
        return dp[0]