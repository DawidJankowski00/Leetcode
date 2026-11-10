using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int MinMoves2(int[] nums) {
            int result = 0;
            Array.Sort(nums);
            int n = nums.Length / 2;
            int tmp = nums[n];
            for(int i = 0; i < n; i++)
            {
                result += tmp - nums[i];
            }
            for(int i = n; i < nums.Length; i++)
            {
                result +=nums[i] - tmp;
            }
            return result;
        }
    }
}
