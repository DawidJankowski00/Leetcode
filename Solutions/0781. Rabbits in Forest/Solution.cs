using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int NumRabbits(int[] answers)
        {
            int result = 0;
            var tmp = new Dictionary<int, int>();
            foreach (int v in answers)
            {
                if (tmp.ContainsKey(v))
                {
                    tmp[v]++;
                }
                else
                {
                    tmp[v] = 1;
                }
            }
            foreach (int v in tmp.Keys)
            {
                result += (v + 1) * ((tmp[v] + v) / (v + 1));
            }
            return result;
        }
    }
}
