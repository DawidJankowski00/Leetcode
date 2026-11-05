using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int FindTheDistanceValue(int[] arr1, int[] arr2, int d) {
            Array.Sort(arr1);
            Array.Sort(arr2);
            int result = 0;
            int j = 0;
            foreach(int v in arr1)
            {
                while (j < arr2.Length && arr2[j] < v - d) j++;

                if (j == arr2.Length || arr2[j] > v + d) result++;
            }
            return result;
        }
    }
}
