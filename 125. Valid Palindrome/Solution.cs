using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public bool IsPalindrome(string s)
        {
            var clean = s.ToLower().Where(x => char.IsLetterOrDigit(x));
            return clean.SequenceEqual(clean.Reverse());
        }
    }
}
