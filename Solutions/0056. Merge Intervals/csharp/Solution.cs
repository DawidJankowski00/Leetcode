using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int[][] Merge(int[][] intervals)
        {
            var result = new List<int[]>();
            Array.Sort(intervals, (a,b) => a[0].CompareTo(b[0]));
            int start = intervals[0][0];
            int stop = intervals[0][1];
            for (int i = 1; i < intervals.Length; i++)
            {
                if (intervals[i][0] <= stop)
                {
                    stop = Math.Max(stop, intervals[i][1]);
                }
                else
                {
                    result.Add(new int[] { start, stop });
                    start = intervals[i][0];
                    stop = intervals[i][1];
                }
            }
            result.Add(new int[] { start, stop });
            return result.ToArray();
        }
    }
}
