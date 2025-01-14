using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int[] FindThePrefixCommonArray(int[] A, int[] B)
        {
            int n = A.Length;
            var result = new int[n];
            var nums = new int[n];
            for (int i = 0; i < n; i++)
            {
                if (i != 0)
                    result[i] = result[i - 1];
                if (A[i] == B[i])
                    result[i]++;
                else
                {
                    if (nums[A[i]-1] == 1)
                        result[i]++;
                    else nums[A[i]-1] = 1;
                    if (nums[B[i] - 1] == 1)
                        result[i]++;
                    else nums[B[i]-1] = 1;
                }
            }
            return result;

        }
    }
}
