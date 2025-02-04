using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int MaxAscendingSum(int[] nums)
        {
            int result = 0;
            int n = nums.Length;
            int tmp = nums[0];

            for (int i = 1; i < n; i++)
            {
                if (nums[i] > nums[i - 1])
                    tmp += nums[i];
                else
                {
                    result = Math.Max(result, tmp);
                    tmp = nums[i];
                }
            }
            return Math.Max(result, tmp);
        }
    }
}
