using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int MinimumSize(int[] nums, int maxOperations)
        {
            int l  = 1;
            int r = nums.Max();
            while (l < r)
            {
                int mid = (l + r) / 2;
                int tmp = 0;
                foreach (int a in nums)
                {
                    tmp += (a - 1) / mid;
                }
                if (tmp > maxOperations)
                {
                    l = mid + 1;
                }
                else
                {
                    r = mid;
                }
            }
            return l;
        }
    }
}
