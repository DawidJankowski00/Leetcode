using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public bool WordPattern(string pattern, string s)
        {
            Dictionary<char, int> dic_s = new Dictionary<char, int>();
            Dictionary<string, int> dic_t = new Dictionary<string, int>();
            string[] st = s.Split(' ');
            if (st.Length != pattern.Length)
            {
                return false;
            }
            for (int i = 0; i < pattern.Length; i++)
            {
                if (!dic_s.ContainsKey(pattern[i]))
                {
                    dic_s.Add(pattern[i], i);
                }
                if (!dic_t.ContainsKey(st[i]))
                {
                    dic_t.Add(st[i], i);
                }
                if (dic_s[pattern[i]] != dic_t[st[i]])
                {
                    return false;
                }
            }
            return true;
        }
    }
}
