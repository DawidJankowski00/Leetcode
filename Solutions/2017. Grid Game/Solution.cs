using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public long GridGame(int[][] grid)
        {
            int n = grid[0].Length;
            long lsum = 0;
            long rsum = 0;
            foreach (var val in grid[0])
            {
                rsum += val;
            }
            long maxpoints = rsum;
            for (int i = 0; i < n; i++)
            {
                rsum -= grid[0][i];
                maxpoints = Math.Min(maxpoints, Math.Max(lsum, rsum));
                lsum += grid[1][i];
            }
            return maxpoints;
        }
    }
}
