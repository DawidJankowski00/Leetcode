using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int FindNumbers(int[] nums)
        {
            int result = 0;
            foreach (int num in nums) 
            {
                result += num.ToString().Length % 2 == 0 ? 1 : 0;
            }
            return result;
        }
    }
}
