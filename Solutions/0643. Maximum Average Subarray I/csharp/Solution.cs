using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public double FindMaxAverage(int[] nums, int k) {
            double curr = 0;
            for (int i = 0; i < k; i++) curr += nums[i];
            double result = curr;
            int n = nums.Length;
            for (int i = k; i < n; i++)
            {
                curr += nums[i] - nums[i - k];
                if (result < curr) result = curr;
            }
            return result / k;
        }
    }
}
