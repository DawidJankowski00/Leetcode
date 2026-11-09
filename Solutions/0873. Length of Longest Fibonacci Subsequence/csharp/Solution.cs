using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int LenLongestFibSubseq(int[] arr)
        {
            int maxct = 0;
            var arrmap = new Dictionary<int, bool>();
            foreach (int v in arr)
            {
                arrmap[v] = true;
            }
            int n = arr.Length;
            for (int i = 0; i < n - 2; i++)
            {
                for (int j = i + 1; j < n - 1; j++)
                {
                    int tmp = 2;
                    int a = arr[i];
                    int b = arr[j];
                    int c = a + b;
                    while (arrmap.ContainsKey(c))
                    {
                        tmp++;
                        a = b;
                        b = c;
                        c = c + a;
                    }
                    if (tmp != 2)
                    {
                        maxct = Math.Max(tmp, maxct);
                    }
                }
            }
            return maxct;
        }
    }
}
