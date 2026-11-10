using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int MinMoves(int[] nums) {
            return nums.Sum() - nums.Min() * nums.Length;
        }
    }
}
