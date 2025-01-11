using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public bool CanConstruct(string s, int k)
        {
            int n = s.Length;
            if (n < k)
                return false;

            var chars = new Dictionary<char, int>();
            foreach (char c in s)
            {
                if (chars.ContainsKey(c))
                    chars[c]++;
                else
                    chars[c] = 1;
            }
            int odds = 0;
            foreach (char c in chars.Keys)
            {
                if (chars[c] % 2 == 1)
                    odds++;
            }
            if (odds > k)
                return false;
            return true;
        }
    }
}
