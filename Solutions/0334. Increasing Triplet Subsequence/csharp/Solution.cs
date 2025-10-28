using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public bool IncreasingTriplet(int[] nums) {
            int l1 = int.MaxValue;
            int l2 = int.MaxValue;
            foreach (int v in nums)
            {
                if (v <= l1) l1 = v;
                else if (v <= l2) l2 = v;
                else return true;
            }
            return false;
        }
    }
}
