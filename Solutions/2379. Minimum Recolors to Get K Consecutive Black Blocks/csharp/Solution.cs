using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int MinimumRecolors(string blocks, int k)
        {
            int curr = blocks[..k].Count(c => c == 'W');
            int l = 0;
            int r = k;
            int result = curr;
            while (r < blocks.Length) 
            {
                if (blocks[l] == 'W')
                    curr--;
                if (blocks[r] == 'W')
                    curr++;
                result = Math.Min(result, curr);
                r++;
                l++;
            }
            return result;
        }
    }
}
