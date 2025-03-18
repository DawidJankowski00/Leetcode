using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int LongestNiceSubarray(int[] nums)
        {
            int result = 1;
            int curr = nums[0];
            int l = 0;
            int r = 1;
            int n = nums.Length;
            while (r < n)
            {
                if ((curr & nums[r]) == 0)
                {
                    curr += nums[r];
                    r++;
                }
                else
                {
                    result = Math.Max(result, r - l);
                    curr -= nums[l];
                    l++;
                }

            }
            result = Math.Max(result, r-l);
            return result;
        }
    }
}
