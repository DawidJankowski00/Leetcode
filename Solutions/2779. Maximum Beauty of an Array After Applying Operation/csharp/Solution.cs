using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int MaximumBeauty(int[] nums, int k)
        {
            Array.Sort(nums);
            int n = nums.Length;
            int result = 0;
            int r = 0;
            for (int l = 0; l < n; l++)
            {
                while (r < n && nums[l] + (2 * k) >= nums[r])
                {
                    r++;
                    if (result < r - l)
                    {
                        result = r - l;
                    }
                }
            }
            return result;
        }
    }
}
