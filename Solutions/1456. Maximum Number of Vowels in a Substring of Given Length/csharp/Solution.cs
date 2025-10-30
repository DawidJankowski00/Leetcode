using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int MaxVowels(string s, int k) {
            HashSet<char> vovels = new HashSet<char> { 'a', 'e', 'i', 'o', 'u' };
            int curr = 0;
            int n = s.Length;
            for (int i = 0; i < k; i++) if (vovels.Contains(s[i])) curr++;
            int result = curr;

            for (int i = k; i < n; i++)
            {
                if (vovels.Contains(s[i])) curr++;
                if (vovels.Contains(s[i - k])) curr--;
                if (curr > result) result = curr;
            }
            return result;   
        }
    }
}
