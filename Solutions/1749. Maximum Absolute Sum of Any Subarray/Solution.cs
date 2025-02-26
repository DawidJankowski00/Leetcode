using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int MaxAbsoluteSum(int[] nums) {
            int curr = 0;
            int maxCurr = 0;
            int minCurr = 0;
            foreach(int v in nums){
                curr += v;
                maxCurr = Math.Max(curr, maxCurr);
                minCurr = Math.Min(curr, minCurr);
            }
            return Math.Abs(maxCurr - minCurr);
        }
    }
}
