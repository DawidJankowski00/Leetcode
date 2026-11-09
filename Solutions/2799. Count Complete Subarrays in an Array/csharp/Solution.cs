using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int CountCompleteSubarrays(int[] nums)
        {
            var all = new Dictionary<int, int>();
            foreach (int i in nums)
            {
                if (all.ContainsKey(i))
                {
                    all[i]++;
                }
                else
                {
                    all[i] = 1;
                }
            }
            int all_ct = all.Count;
            int n = nums.Length;
            int result = 0;
            var curr = new Dictionary<int, int>();
            int l = 0;

            for (int r = 0; r < n; r++)
            {
                if (!curr.ContainsKey(nums[r]))
                {
                    curr[nums[r]] = 0;
                }
                curr[nums[r]]++;
                while (curr.Count == all_ct)
                {
                    curr[nums[l]]--;
                    if (curr[nums[l]] == 0)
                    {
                        curr.Remove(nums[l]);
                    }
                    l++;
                    result += n - r;
                }
            }


            return result;
        }
    }
}
