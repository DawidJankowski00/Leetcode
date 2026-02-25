using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int[] SortByBits(int[] arr) {
            return arr.OrderBy(x => BitOperations.PopCount((uint)x)).ThenBy(x => x).ToArray();
        }
    }
}
