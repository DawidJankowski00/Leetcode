using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int CountGoodStrings(int low, int high, int zero, int one)
        {
            int result = 0;
            int mod = 1_000_000_007;
            int[] dp = new int[high + 1];
            dp[0] = 1;

            for (int i = Math.Min(zero, one); i <= high; i++)
            {
                if (i >= zero)
                {
                    dp[i] = (dp[i] + dp[i - zero]) % mod;
                }
                if (i >= one)
                {
                    dp[i] = (dp[i] + dp[i - one]) % mod;
                }
            }
            for (int i = low; i <= high; i++)
            {
                result = (result + dp[i]) % mod;
            }
            return result;
        }
    }
}
