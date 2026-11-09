using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int MaxChunksToSorted(int[] arr)
        {
            int n = arr.Length;
            int curr = 0;
            int needed_sum = 0;
            int result = 0;
            for (int i = 0; i < n; i++)
            {
                needed_sum += i;
                curr += arr[i];
                if (needed_sum == curr)
                {
                    result += 1;
                }
            }
            return result;
        }
    }
}
