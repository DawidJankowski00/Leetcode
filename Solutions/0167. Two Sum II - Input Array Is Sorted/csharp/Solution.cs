using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int[] TwoSum(int[] numbers, int target)
        {
            int l = 0;
            int r = numbers.Length -1;
            while (l != r)
            {
                if (numbers[l] + numbers[r] == target)
                {
                    return [l + 1, r + 1];
                }
                else if (numbers[l] + numbers[r] > target) { r--; }
                else { l++; }
            }
            return [];
        }
    }
}
