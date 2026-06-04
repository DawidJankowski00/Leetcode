using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        private const int MAX = 100001;
        private static readonly int[] dp = new int[MAX];
        private static readonly int[] prefixSum = new int[MAX];
        static Solution() {
            for (int i = 100; i < MAX; i++) {
                int r = i % 10;
                int m = (i / 10) % 10;
                int l = (i / 100) % 10;

                bool isWavy = (l < m && m > r) || (l > m && m < r);
                dp[i] = dp[i / 10] + (isWavy ? 1 : 0);
                prefixSum[i] = prefixSum[i - 1] + dp[i];
            }
        }
        public int TotalWaviness(int num1, int num2) {
            return prefixSum[num2] - prefixSum[num1 -1];
        }
    }
}
