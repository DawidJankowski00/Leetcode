using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public long CountBadPairs(int[] nums)
        {
            int n = nums.Length;
            long result = ((long)n * (n - 1)) / 2;
            var freq = new Dictionary<int, int>();
            for (int i = 0; i < n; i++) {
                int tmp = nums[i] - i;
                if (!freq.ContainsKey(tmp))
                {
                    freq[tmp] = 0;
                }
                result -= freq[tmp];
                freq[tmp]++;
            }
            return result;
        }
    }
}
