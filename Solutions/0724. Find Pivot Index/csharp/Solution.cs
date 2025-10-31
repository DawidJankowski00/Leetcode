using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int PivotIndex(int[] nums) {
            int total_sum = 0;
            foreach (int v in nums) total_sum += v;
            int left_sum = 0;
            for (int i = 0; i < nums.Length; i++)
            {
                int right_sum = total_sum - left_sum - nums[i];
                if (left_sum == right_sum) return i;
                left_sum += nums[i];
            }
            return -1;
        }
    }
}
