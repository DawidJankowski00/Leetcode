using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int MinMoves(int[] nums) {
            int x = 0;
            int y = 0;
            int n = nums.Length;
            foreach(int v in nums)
            {
                x += v;
                if(y < v) y = v;
            }
            return n * y - x;
        }
    }
}
