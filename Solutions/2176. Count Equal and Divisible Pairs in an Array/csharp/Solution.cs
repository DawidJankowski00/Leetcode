using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int CountPairs(int[] nums, int k) {
            int n = nums.Length;
            int result = 0;
            for (int i = 0; i < n-1; i++)
            {
                for (int j = i+1; j < n; j++)
                {
                    if (nums[i] == nums[j] && (i * j) % k == 0) result++;
                }
            }
            return result;
        }
    }
}
