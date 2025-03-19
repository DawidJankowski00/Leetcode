using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int MinOperations(int[] nums)
        {
            int n = nums.Length;
            int result = 0;
            for (int i = 0; i < n - 2; i++)
            {
                if (nums[i] == 0)
                {
                    result++;
                    nums[i] = 1;
                    nums[i + 1] = 1 - nums[i + 1];
                    nums[i + 2] = 1 - nums[i + 2];
                }
            }
            if (nums[^1] == 1 && nums[^2] == 1)
                return result;
            return -1;
        }
    }
}
