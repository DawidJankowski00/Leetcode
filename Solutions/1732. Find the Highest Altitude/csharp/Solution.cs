using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int LargestAltitude(int[] gain) {
            int result = 0;
            int curr = 0;
            foreach (int v in gain)
            {
                curr += v;
                if (result < curr) result = curr;
            }
            return result;
        }
    }
}
