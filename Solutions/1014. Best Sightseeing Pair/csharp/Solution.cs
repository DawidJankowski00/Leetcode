using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int MaxScoreSightseeingPair(int[] values)
        {
            int dp = 0;
            int score = 0;
            for (int i = 0; i < values.Length; i++)
            {
                score = Math.Max(score, dp + values[i] - i);
                dp = Math.Max(dp, values[i] + i);
            }
            return score;
        }
    }
}
