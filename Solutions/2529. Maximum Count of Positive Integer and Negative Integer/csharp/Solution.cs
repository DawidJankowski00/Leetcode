using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    using System;
    using System.Collections.Generic;
    using System.Linq;
    
    using System;
    using System.Collections.Generic;
    using System.Linq;

    public class Solution {
        public int MaximumCount(int[] nums) {
            int n = nums.Length;
            int l = 0;
            int i = 0;
            while (i < n && nums[i] <= 0){
                if (nums[i] != 0)
                    l++;
                i++;
            }
            return Math.Max(l, n-i);
        }
    }
}
