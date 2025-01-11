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

            var charArray = new int[26]; 
            foreach (char c in s)
            {
                charArray[c - 'a']++;
            }
            int odds = 0;
            foreach (int c in charArray)
            {
                if (c % 2 == 1)
                    odds++;
            }
            if (odds > k)
                return false;
            return true;
        }
    }
}
