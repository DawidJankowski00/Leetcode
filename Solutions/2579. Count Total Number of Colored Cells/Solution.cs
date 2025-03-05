using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public long ColoredCells(int n) {
            return (long)2 * n * (n-1) + 1;
        }
    }
}
