using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public bool DoesValidArrayExist(int[] derived)
        {
            int result = 0;
            foreach (int i in derived)
            {
                result ^= i;
            }
            return result == 0;
        }
    }
}
