using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int LongestMonotonicSubarray(int[] nums)
        {
            int result = 0;
            int tmp_dec = 1;
            int tmp_inc = 1;
            for (int i = 1; i < nums.Length; i++)
            {
                if (nums[i - 1] < nums[i])
                {
                    tmp_dec++;
                }
                else
                {
                    if (tmp_dec > result)
                        result = tmp_dec;
                    tmp_dec = 1;
                }
                if (nums[i - 1] > nums[i])
                {
                    tmp_inc++;
                }
                else
                {
                    if (tmp_inc > result)
                        result = tmp_inc;
                    tmp_inc = 1;
                }
            }
            return Math.Max(result, Math.Max(tmp_dec, tmp_inc));
        }
    }
}
