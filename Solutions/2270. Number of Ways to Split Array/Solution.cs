using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int WaysToSplitArray(int[] nums)
        {
            int result = 0;
            int cur_sum_r = 0;
            foreach (var v in nums)
            {
                cur_sum_r += v;
            }
            int cur_sum_l = 0;
            for (int i = 0; i < nums.Length - 1; i++)
            {
                cur_sum_l += nums[i];
                cur_sum_r -= nums[i];
                if (cur_sum_l >= cur_sum_r) result++;
            }
            return result;
        }
    }
}
