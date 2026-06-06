using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int[] LeftRightDifference(int[] nums) {
            int l = 0;
            int r = 0;
            for (int i = 0; i < nums.Length; i++) {
                r += nums[i];
            }
            int[] ans = new int[nums.Length];
            for (int i = 0; i < nums.Length; i++) {
                r -= nums[i];
                ans[i] = Math.Abs(l - r);
                l += nums[i];
            }
            return ans;
        }
    }
}
