using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public bool Check(int[] nums)
        {
            int n = nums.Length;
            int[] result = (int[])nums.Clone();
            Array.Sort(result);
            for (int i = 0; i < n; i++)
            {
                if (Enumerable.SequenceEqual(result, Rotate(nums,i)))
                {
                    return true;
                }
            }
            return false;
        }
        private int[] Rotate(int[] nums, int x) 
        {
            int n = nums.Length;
            int[] result = new int[n];

            for (int i = 0; i < n; i++)
            {
                result[i] = nums[(i+x) % n];
            }
            return result;
        }

    }
}
