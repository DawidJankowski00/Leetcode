using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int Compress(char[] chars) {
            int l1 = 0;
            int l2 = 0;
            int curr = 0;
            int n = chars.Length;
            while (l2 < n)
            {
                while (l2 < n && chars[l2] == chars[curr]) l2++;
                int ct = l2 - curr;
                chars[l1] = chars[curr];
                l1++;
                if (ct > 1)
                {
                    string tmp = ct.ToString();
                    foreach (char v in tmp)
                    {
                        chars[l1] = v;
                        l1++;
                    }
                }
                curr = l2;
            }
            return l1;
        }
    }
}
