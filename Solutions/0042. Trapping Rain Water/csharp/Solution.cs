using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int Trap(int[] height)
        {
            int r = height.Length - 1;
            int l = 0;
            int maxright = height[r];
            int maxleft = height[l];
            int water = 0;
            while (r != l)
            {
                if (height[r] <= height[l])
                {
                    r -= 1;
                    if (maxright < height[r])
                    {
                        maxright = height[r];
                    }
                    water += maxright - height[r];
                }
                else
                {
                    l += 1;
                    if (maxleft < height[l])
                    {
                        maxleft = height[l];
                    }
                    water += maxleft - height[l];
                }
            }
            return water;
        }
    }
}
