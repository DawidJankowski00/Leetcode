using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int[] ProductExceptSelf(int[] nums) {
            int n = nums.Length;
            int pre = 1;
            int[] result = new int[n];

            for (int i = 0; i < n; i++)
            {
                result[i] = pre;
                pre *= nums[i];
            }
            int post = 1;
            for (int i = n - 1; i >= 0; i--)
            {
                result[i] *= post;
                post *= nums[i];
            }
            return result;
        }
    }
}
