using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int EarliestFinishTime(int[] landStartTime, int[] landDuration, int[] waterStartTime, int[] waterDuration) {
            int result = int.MaxValue;
            int minL = int.MaxValue;
            int minW = int.MaxValue;
            int n = landStartTime.Length;
            int m = waterStartTime.Length;
            for (int i = 0; i < n; i++)
            {
                minL = Math.Min(minL, landStartTime[i] + landDuration[i]);
            }
            for (int i = 0; i < m; i++)
            {
                minW = Math.Min(minW, waterStartTime[i] + waterDuration[i]);
                result = Math.Min(result, Math.Max(minL, waterStartTime[i]) + waterDuration[i]);
            }
            for (int i = 0; i < n; i++)
            {
                result = Math.Min(result, Math.Max(minW, landStartTime[i]) + landDuration[i]);
            }
            return result;

        }
    }
}
