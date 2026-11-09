using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int NumOfSubarrays(int[] arr) {
            long mod = 1_000_000_007;
            long curr = 0;
            long ct = 0;
            foreach(int v in arr){
                curr += v;
                ct += curr % 2;
            }
            ct += (arr.Length - ct) * ct;
            return (int)(ct % mod);
        }
    }
}
