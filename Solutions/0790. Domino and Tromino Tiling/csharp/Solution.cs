using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int NumTilings(int n) {
            long[] dp = new long[n + 3];
            dp[0] = 1;
            dp[1] = 2;
            dp[2] = 5;
            for (int i = 3; i < n; i++) dp[i] = (dp[i-1] * 2 + dp[i-3]) % 1000000007;
            return (int )dp[n - 1];
        }
    }
}
