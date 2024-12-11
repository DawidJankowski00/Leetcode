using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Intrinsics.X86;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int MaximumLength(string s)
        {
            int n = s.Length;
            int l = 1;
            int r = n;

            if (!helper(s, n, l))
            {
                return -1;
            }

            while (l + 1 < r)
            {
                int mid = (l + r) / 2;
                if (helper(s, n, mid)) { l = mid; }
                else { r = mid; }
            }

            return l; 
        }
        public bool helper(string s, int n, int x)
        {
            Dictionary<char, int> dic = new Dictionary<char, int>();
            int p = 0;
            for (int i = 0; i < n; i++)
            {
                while (s[p] != s[i])
                {
                    p++;
                }
                if ((i - p + 1) >= x)
                {
                    if (dic.ContainsKey(s[i]))
                    {
                        dic[s[i]]++;
                    }
                    else
                    {
                        dic.Add(s[i], 1);
                    }
                    if (dic[s[i]] > 2)
                    {
                        return true;
                    }
                }
            }
            return false;
        }
    }
}
