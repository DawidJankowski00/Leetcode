using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int MinElement(int[] nums) {
            int result = int.MaxValue;
            foreach (var v in nums)
            {
                int sum = GetDigitSum(v);
                if (sum < result) result = sum;
            }
            return result;

        }

        private int GetDigitSum(int n)
        {
            int result = 0;
            while (n > 0)
            {
                result += n % 10;
                n /= 10;
            }
            return result;
        }
    }
}
