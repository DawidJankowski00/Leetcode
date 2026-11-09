using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public long MaximumTripletValue(int[] nums)
        {
            long maxValue = 0;
            long maxDiff = 0;
            long result = 0;
            foreach (int num in nums)
            {
                result = Math.Max(result, maxDiff * num);
                maxDiff = Math.Max(maxDiff, maxValue - num);
                maxValue = Math.Max(maxValue, num);
            }
            return result;
        }
    }
}
