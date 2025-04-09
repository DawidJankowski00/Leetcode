using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int MinimumOperations(int[] nums)
        {
            HashSet<int> ht = new HashSet<int>();
            for (int i = nums.Length - 1; i >= 0; i--)
            {
                if (ht.Contains(nums[i]))
                    return i / 3 + 1;
                ht.Add(nums[i]);
            }
            return 0;
        }
    }
}
