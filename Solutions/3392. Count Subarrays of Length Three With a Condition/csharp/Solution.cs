using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int CountSubarrays(int[] nums) {
            int n = nums.Length;
            int result = 0;
            for(int i = 0; i < n-2; i++){
                if((nums[i] + nums[i+2]) * 2 == nums[i+1]) result++;
            }
            return result;
        }
    }
}
