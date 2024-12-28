using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public bool CanConstruct(string ransomNote, string magazine)
        {
            Dictionary<char, int> dic = new Dictionary<char, int>();
            foreach(char s in magazine) 
            {
                if (dic.ContainsKey(s))
                {
                    dic[s]++;
                }
                else
                {
                    dic.Add(s, 1);
                }
            }
            foreach (char s in ransomNote)
            {
                if (!dic.ContainsKey(s) || dic[s] == 0)
                {
                    return false;
                }
                dic[s]--;
            }
            
            return true;             
        }
    }
}
