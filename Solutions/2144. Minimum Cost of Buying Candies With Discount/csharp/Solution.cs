using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int MinimumCost(int[] cost) {
            int result = 0;
            Array.Sort(cost);
            int j = 0;
            for (int i = cost.Length - 1; i >= 0; i--)
            {
                if (j == 2)
                {
                    j = 0;
                    continue;
                }
                result += cost[i];
                j++;
            }
            return result;
        }
    }
}
