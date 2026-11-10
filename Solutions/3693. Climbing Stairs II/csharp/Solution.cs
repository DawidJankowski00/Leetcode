public class Solution {
    public int ClimbStairs(int n, int[] costs) {
        costs = [0, ..costs];

        int inf = int.MaxValue / 2;
        int[] dp = Enumerable.Repeat(inf, n+3).ToArray();
        dp[n] = costs[n];

        for (int i = n-1; i >= 0; i--)
        {
            dp[i] = costs[i] + Math.Min(dp[i+1] + 1, Math.Min(dp[i+2] + 4, dp[i+3] + 9));
        }
        return dp[0];
    }
}
