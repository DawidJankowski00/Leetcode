using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public IList<string> SummaryRanges(int[] nums)
        {
            List<string> result = new List<string>();
            int l = 0;
            int last = 0;
            if (nums.Length == 0) return result;
            for (int i = 1; i < nums.Length; i++)
            {
                if (nums[i] == nums[last] + 1) last = i;
                else
                {
                    if (last - l == 0) result.Add(nums[l].ToString());
                    else result.Add(nums[l].ToString() + "->" + nums[last].ToString());
                    l = i;
                    last = i;
                }
                
            }
            if (last - l == 0) result.Add(nums[l].ToString());
            else result.Add(nums[l].ToString() + "->" + nums[last].ToString());
            return result;
        }
    }
}
