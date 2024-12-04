using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int MinSubArrayLen(int target, int[] nums)
        {
            if (nums.Sum(x => x) < target) return 0;
            int result = nums.Length;
            int l = 0;
            int tmp = 0;
            int curr = 0;

            for (int r = 0; r < nums.Length; r++)
            {
                tmp += nums[r];
                while (tmp >= target)
                {
                    tmp -= nums[l];
                    result = int.Min(result, r-l+1);
                    l++;
                }
            }

            return result;
        }
    }
}
