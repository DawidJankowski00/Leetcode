using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public IList<IList<string>> GroupAnagrams(string[] strs)
        {
            Dictionary<string, List<string>> dic = new Dictionary<string, List<string>>();
            foreach (string str in strs)
            {
                char[] chars = str.ToCharArray();
                Array.Sort(chars);
                string sortedStr = new string(chars);

                if (!dic.ContainsKey(sortedStr))
                {
                    dic[sortedStr] = new();
                }
                dic[sortedStr].Add(str);
            }
            return dic.Values.Select(group => (IList<string>)group).ToList();
        }
    }
}
