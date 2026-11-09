using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int[] PivotArray(int[] nums, int pivot)
        {
            List<int> lower = new List<int>();
            List<int> equal = new List<int>();
            List<int> greather = new List<int>();
            foreach (int v in nums)
            {
                if (v < pivot)
                {
                    lower.Add(v);
                }
                else if (v == pivot)
                {
                    equal.Add(v);
                }
                else
                {
                    greather.Add(v);
                }
            }
            return lower.Concat(equal).Concat(greather).ToArray();
        }
    }
}
