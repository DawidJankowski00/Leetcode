using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int[][] Insert(int[][] intervals, int[] newInterval)
        {
            var allIntervals = new List<int[]>(intervals);
            allIntervals.Add(newInterval);
            var result = new List<int[]>();
            allIntervals.Sort((a, b) => a[0].CompareTo(b[0]));
            int start = allIntervals[0][0];
            int stop = allIntervals[0][1];
            for (int i = 1; i < allIntervals.Count; i++)
            {
                if (allIntervals[i][0] <= stop)
                {
                    stop = Math.Max(stop, allIntervals[i][1]);
                }
                else
                {
                    result.Add(new int[] { start, stop });
                    start = allIntervals[i][0];
                    stop = allIntervals[i][1];
                }
            }
            result.Add(new int[] { start, stop });
            return result.ToArray();
        }
    }
}
