using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public string ShiftingLetters(string s, int[][] shifts)
        {
            int n = s.Length;
            int[] shift = new int[n+1];
            for (int i = 0; i < n + 1; i++)
            {
                shift[i] = 0;
            }
            foreach (int[] v in shifts)
            {
                int l = 1;
                int r = -1;
                if (v[2] == 0)
                {
                    l = -1;
                    r = 1;
                }
                shift[v[0]] += l;
                shift[v[1] + 1] += r;
            }
            int curr = 0;
            char[] result = s.ToCharArray();
            for (int i = 0; i < n; i++)
            {
                curr += shift[i];
                result[i] = (char)('a' + ((result[i] - 'a' + curr % 26 + 26) % 26));
            }
            return new string(result);
        }
    }
}
