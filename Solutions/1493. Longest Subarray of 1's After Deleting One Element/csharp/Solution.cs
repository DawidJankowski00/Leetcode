using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int LongestSubarray(int[] nums) {
            int l = 0;
            int k = 1;
            int n = nums.Length;
            int r1 = 0;
            for (int r = 0; r < n; r++)
            {
                if (nums[r] == 0) k--;
                if (k < 0)
                {
                    if (nums[l] == 0) k++;
                    l++;
                }
                r1 = r;
            }
            return r1 - l;
        }
    }
}
