using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int MinEatingSpeed(int[] piles, int h) {
            int left = 1;
            int right = piles.Max();
            int result = right;
            while (left <= right)
            {
                int mid = (left + right) / 2;
                long hours = 0;
                foreach (var pile in piles)
                {
                    hours += (pile + mid - 1) / mid;
                }
                if (hours > h)
                {
                    left = mid + 1;
                }
                else
                {
                    right = mid-1;
                    result = mid;
                }
            }
            return result;
        }
    }
}
