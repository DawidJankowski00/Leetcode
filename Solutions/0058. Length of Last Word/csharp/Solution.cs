using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int LengthOfLastWord(string s)
        {
            
            string ne= s.Trim().Split(' ').Last();
            return ne.Length;
        }
    }
}
