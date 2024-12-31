using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int LongestConsecutive(int[] nums)
        {
            Array.Sort(nums);
            int result = 0;
            int? last = null;
            int tmp = 0;
            foreach (int i in nums)
            {
                if (last == i) continue;
                if (i - 1 == last)
                {
                    tmp++;
                }
                else
                {
                    if (result < tmp)
                    {
                        result = tmp;
                    }
                    tmp = 1;
                }
                last = i;
            }
            if (result < tmp)
            {
                result = tmp;
            }
            return result;
        }
    }
}
