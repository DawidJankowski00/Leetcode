using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public bool IsAnagram(string s, string t)
        {
            Dictionary<char, int> dict_s = new Dictionary<char, int>();
            foreach (char c in s)
            {
                if (dict_s.ContainsKey(c))
                {
                    dict_s[c]++;
                }
                else
                {
                    dict_s.Add(c, 1);
                }
            }
            foreach (char c in t)
            {
                if (!dict_s.ContainsKey(c)) return false;
                else
                {
                    dict_s[c]--;
                    if (dict_s[c] == 0)
                    {
                        dict_s.Remove(c);
                    }
                }
            }
            return dict_s.Count == 0;
        }
    }
}
