using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int MaximumSum(int[] nums)
        {
            int result = -1;
            var map = new Dictionary<int, int>();
            foreach (var item in nums)
            {
                int tmp = item;
                int Digit_Sum = 0;
                while (tmp >= 10)
                {
                    Digit_Sum += tmp % 10;
                    tmp /= 10;
                }
                Digit_Sum += tmp;
                if (map.ContainsKey(Digit_Sum))
                {
                    tmp = map[Digit_Sum];
                    if (result < tmp + item)
                        result = tmp + item;
                    if (tmp < item)
                        map[Digit_Sum] = item;
                }
                else
                    map[Digit_Sum] = item;
            }
            return result;
        }
    }
}
