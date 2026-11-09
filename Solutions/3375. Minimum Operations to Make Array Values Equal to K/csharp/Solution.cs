using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int MinOperations(int[] nums, int k)
        {
            int tmp = nums.Min();
            if (tmp < k)
            {
                return -1;
            }
            int result = new HashSet<int>(nums).Count + (tmp > k ? 1 : 0) - 1;
            return result;
        }
    }
}
