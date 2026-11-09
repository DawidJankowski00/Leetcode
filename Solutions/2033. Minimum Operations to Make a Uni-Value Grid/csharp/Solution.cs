using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int MinOperations(int[][] grid, int x)
        {
            var values = new List<int>();
            var tmp = grid[0][0] % x;
            foreach (var row in grid)
            {
                foreach (var v in row) {
                    if (v % x == tmp)
                    {
                        values.Add(v);
                    }
                    else {
                        return -1;      
                    }
                }
            }
            values.Sort();
            var median = values[values.Count / 2];
            int result = 0;
            foreach (int v in values)
            {
                result += Math.Abs(median - v) / x;
            }
            return result;
        }
    }
}
