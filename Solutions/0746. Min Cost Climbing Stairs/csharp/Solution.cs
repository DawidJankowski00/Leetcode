using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int MinCostClimbingStairs(int[] cost) {
            cost.Append(0);
            for (int i = cost.Length - 3; i >= 0; i--)
            {
                cost[i] = cost[i] + Math.Min(cost[i + 1], cost[i + 2]);
            }
            return Math.Min(cost[0], cost[1]);
        }
    }
}
