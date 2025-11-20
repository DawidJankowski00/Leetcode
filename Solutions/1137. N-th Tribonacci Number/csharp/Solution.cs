using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int Tribonacci(int n) {
            Dictionary<int, int> dp = new Dictionary<int, int>();
            dp[0] = 0;
            dp[1] = 1;
            dp[2] = 1;
            int helper(int k)
            {
                if (dp.ContainsKey(k))
                {
                    return dp[k];
                }
                dp[k] = helper(k - 1) + helper(k - 2) + helper(k - 3);
                return dp[k];
            }
            return helper(n);
        }
    }
}
