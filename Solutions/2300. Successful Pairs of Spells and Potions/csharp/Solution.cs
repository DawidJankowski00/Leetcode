using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int[] SuccessfulPairs(int[] spells, int[] potions, long success) {
            Array.Sort(potions);
            int n = potions.Length;
            int[] result = new int[spells.Length];
            for (int i = 0;i < spells.Length;i++)
            {
                int v = spells[i];
                long neded = (success + v - 1) / v;
                result[i] = n - LowerBound(potions, neded);
            }
            return result;
        }
        private int LowerBound(int[] arr, long target)
        {
            int left = 0;
            int right = arr.Length;
            while (left < right)
            {
                int mid = left + (right - left) / 2;
                if (arr[mid] < target)
                {
                    left = mid + 1;
                }
                else
                {
                    right = mid;
                }
            }
            return left;
        }
    }
}
