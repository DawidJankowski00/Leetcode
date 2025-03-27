using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int MinimumIndex(IList<int> nums)
        {
            Dictionary<int, int> right = new Dictionary<int, int>();
            int l_n = 0;
            int r_n = nums.Count;
            foreach (int i in nums)
            {
                if (right.ContainsKey(i))
                {
                    right[i]++;
                }
                else
                {
                    right.Add(i, 1);
                }
            }
            int element = -1;
            int r_element_ct = -1;
            foreach (int i in right.Keys)
            {
                if (right[i] > r_element_ct)
                {
                    element = i;
                    r_element_ct = right[i];
                }

            }
            int l_element_ct = 0;
            if (r_element_ct * 2 <= r_n)
                return -1;
            for (int i = 0; i < nums.Count; i++)
            {
                if (nums[i] == element)
                {
                    l_element_ct++;
                    r_element_ct--;
                }
                l_n++;
                r_n--;
                if (l_element_ct * 2 > l_n && r_element_ct * 2 > r_n)
                    return i;
            }
            return -1;

        }
    }
}
