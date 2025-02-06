using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int TupleSameProduct(int[] nums)
        {
            int n = nums.Length;
            int result = 0;
            var freq = new Dictionary<int, int>();
            for (int i = 0; i < n; i++)
            {
                for (int j = i + 1; j < n; j++) 
                {
                    int tmp = nums[j] * nums[i];
                    if (freq.ContainsKey(tmp))
                    {
                        result += freq[tmp];
                    }
                    else
                    {
                        freq[tmp] = 0;
                    }
                    freq[tmp]++;

                }
            }
            return result * 8;
        }
    }
}
