using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public long MaxTotalValue(int[] nums, int k) {
            int m1 = int.MinValue, m2 = int.MaxValue;
            foreach (var n in nums)
            {
                m1 = Math.Max(m1, n);
                m2 = Math.Min(m2, n);
            }
            return (long)(m1 - m2) * k;
        }
    }
}
