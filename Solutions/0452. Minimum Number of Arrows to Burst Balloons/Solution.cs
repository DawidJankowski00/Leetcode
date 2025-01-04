using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int FindMinArrowShots(int[][] points)
        {
            int result = 1;
            Array.Sort(points,(a,b) => a[1].CompareTo(b[1]));
            int stop = points[0][1];
            for (int i = 1; i < points.Length; i++)
            {
                if (points[i][0] <= stop)
                {
                    if (points[i][1] < stop) stop = points[i][1];
                    continue;
                }
                else
                {
                    stop = points[i][1];
                    result++;
                }
            }
            return result;
        }
    }
}
