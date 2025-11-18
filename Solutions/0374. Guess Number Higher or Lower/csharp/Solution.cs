using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution : GuessGame {
        public int GuessNumber(int n) {
            int start = 1;
            while (true)
            {
                int mid = start + (n-start) / 2;
                int res = guess(mid);
                if (res == 0) return mid;
                else if (res == -1) n = mid-1;
                else start = mid + 1;
            }
        }
    }
}
