using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int XorAllNums(int[] nums1, int[] nums2)
        {
            int result = 0;
            int result2 = 0;
            int n = nums1.Length;
            int m = nums2.Length;
            if (n % 2 == 1)
            {
                foreach (int v in nums2)
                {
                    result2 ^= v;
                }
            }
            if (m % 2 == 1)
            {
                foreach (int v in nums1)
                {
                    result ^= v;
                }
            }
            return result ^ result2;
        }
    }
}
