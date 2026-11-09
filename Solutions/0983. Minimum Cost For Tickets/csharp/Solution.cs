using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int MincostTickets(int[] days, int[] costs)
        {
            int n = days[^1];
            int[] dp = new int[n + 1];
            HashSet<int> dy = new HashSet<int>(days);
           
            for (int i = 1; i < n + 1; i++)
            {
                if (!dy.Contains(i))
                {
                    dp[i] = dp[i - 1];
                }
                else
                {
                    dp[i] = Math.Min(Math.Min(dp[i - 1] + costs[0], i >= 7 ? dp[i - 7] + costs[1] : costs[1]), i >= 30 ? dp[i - 30] + costs[2] : costs[2]);
                }
            }
            return dp[^1];
        }
    }
}
