using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int FindPeakElement(int[] nums) {
            int first = 0;
            int last = nums.Length - 1;
            while (first < last)
            {
                int mid = first + (last - first + 1) / 2;
                if (nums[mid] < nums[mid - 1])
                {
                    last = mid - 1;
                }
                else
                {
                    first = mid;
                }
            }
            return first;
        }
    }
}
