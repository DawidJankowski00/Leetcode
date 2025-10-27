using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public string ReverseVowels(string s) {
            HashSet<char> vowels = new HashSet<char> { 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' };
            char[] sArray = s.ToCharArray();
            int l = 0;
            int r = sArray.Length - 1;
            while (l < r)
            {
                if (!vowels.Contains(sArray[l])) l++;
                else if (!vowels.Contains(sArray[r])) r--;
                else
                {
                    char tmp = sArray[l];
                    sArray[l] = sArray[r];
                    sArray[r] = tmp;
                    l++;
                    r--;
                }
            }
            return new string(sArray);
        }
    }
}
