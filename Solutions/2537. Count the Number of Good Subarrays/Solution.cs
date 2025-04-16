using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public long CountGood(int[] nums, int k)
        {
            long result = 0;
            int n = nums.Length;
            int l = 0;
            var curr = new Dictionary<int, int>();
            int curr_pairs = 0;

            for (int r = 0; r < n; r ++)
            {
                if (!curr.ContainsKey(nums[r]))
                    curr[nums[r]] = 0;
                curr_pairs += curr[nums[r]];
                curr[nums[r]]++;

                while (curr_pairs >= k)
                {
                    result += n - r;
                    curr[nums[l]]--;
                    curr_pairs -= curr[nums[l]];
                    l += 1;
                }
            }

            return result;
        }
    }
}
