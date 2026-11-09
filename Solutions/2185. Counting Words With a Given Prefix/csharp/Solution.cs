using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int PrefixCount(string[] words, string pref) {
            int result = 0;
            foreach (string v in words){
                if (v.Startwith(pref))
                    result++;
            }
            return result;
        }
    }
}
