using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public bool IsIsomorphic(string s, string t)
        {
            Dictionary<char, int> dic_s = new Dictionary<char, int>();
            Dictionary<char, int> dic_t = new Dictionary<char, int>();
            for (int i = 0; i < s.Length; i++)
            {
                if (!dic_s.ContainsKey(s[i]))
                {
                    dic_s.Add(s[i], i);
                }
                if (!dic_t.ContainsKey(t[i]))
                {
                    dic_t.Add(t[i], i);
                }
                if (dic_s[s[i]] != dic_t[t[i]])
                {
                    return false;
                }
            }
            return true;
        }
    }
}
