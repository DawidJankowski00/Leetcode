using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public long FindScore(int[] nums)
        {
            int n  = nums.Length;
            var sortedNums = nums
            .Select((value, index) => (Value: value, Index: index))
            .OrderBy(pair => pair.Value)
            .ToList();

            long result = 0;
            foreach (var (num, i) in sortedNums)
            {
                if (nums[i] != -1)
                {
                    result += num;
                    nums[i] = -1;
                    if (i > 0)
                    {
                        nums[i - 1] = -1;
                    }
                    if (i < n - 1)
                    {
                        nums[i + 1] = -1;
                    }
                }
            }
            return result;
        }
    }
}
