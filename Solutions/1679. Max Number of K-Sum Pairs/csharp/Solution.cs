using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int MaxOperations(int[] nums, int k) {
            int result = 0;
            Array.Sort(nums);
            int l = 0;
            int r = nums.Length - 1;
            while (l < r)
            {
                int tmp = nums[l] + nums[r];
                if (tmp == k)
                {
                    result++;
                    l++;
                    r--;
                    continue;
                }
                if (tmp > k) r--;
                else l++;
            }
            return result;
        }
    }
}
