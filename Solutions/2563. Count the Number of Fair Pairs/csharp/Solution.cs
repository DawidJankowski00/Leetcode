using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public long CountFairPairs(int[] nums, int lower, int upper) {
            Array.Sort(nums);
            int l = 0;
            int r = nums.Length - 1;
            long result = 0;

            // Liczymy pary, których suma <= upper
            while (l < r) {
                if (nums[l] + nums[r] <= upper) {
                    result += r - l;
                    l++;
                } else {
                    r--;
                }
            }

            // Reset wskaźników
            l = 0;
            r = nums.Length - 1;

            // Odejmujemy pary, których suma < lower
            while (l < r) {
                if (nums[l] + nums[r] < lower) {
                    result -= r - l;
                    l++;
                } else {
                    r--;
                }
            }

            return result;
        }
    }
}
