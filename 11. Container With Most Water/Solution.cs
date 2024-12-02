using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int MaxArea(int[] height)
        {
            int l = 0;
            int r = height.Length - 1;
            int maxAmount = 0;
            while (l < r)
            {
                if (maxAmount < int.Min(height[l], height[r]) * (r - l))
                {
                    maxAmount = int.Min(height[l], height[r]) * (r - l);
                }
                if (height[l] > height[r])
                {
                    r -= 1;
                }
                else
                {
                    l += 1;
                }
            }
            return maxAmount;
        }
    }
}
