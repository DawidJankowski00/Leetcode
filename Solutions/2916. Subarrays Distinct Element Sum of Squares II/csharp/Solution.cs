using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    using System;
    using System.Collections.Generic;

    public class Solution {
        private long[] bit1;
        private long[] bit2;
        private int n;
        private const long MOD = 1_000_000_007;

        public int SumCounts(int[] nums) {
            n = nums.Length;
            bit1 = new long[n + 2];
            bit2 = new long[n + 2];
            
            int[] lastPos = new int[100005];
            Array.Fill(lastPos, -1);

            long totalAns = 0;
            long curSqSum = 0;

            for (int i = 0; i < n; i++) {
                int x = nums[i];
                int p = lastPos[x];

                int l = p + 2;
                int r = i + 1;

                long s = RangeSum(l, r);

                curSqSum = (curSqSum + 2 * s + (r - l + 1)) % MOD;
                totalAns = (totalAns + curSqSum) % MOD;

                RangeAdd(l, r, 1);
                lastPos[x] = i;
            }

            return (int)totalAns;
        }

        private void Add(long[] bit, int idx, long val) {
            while (idx <= n + 1) {
                bit[idx] += val;
                idx += idx & -idx;
            }
        }

        private long Query(long[] bit, int idx) {
            long sum = 0;
            while (idx > 0) {
                sum += bit[idx];
                idx -= idx & -idx;
            }
            return sum;
        }

        private void RangeAdd(int l, int r, long val) {
            Add(bit1, l, val);
            Add(bit1, r + 1, -val);
            Add(bit2, l, val * (l - 1));
            Add(bit2, r + 1, -val * r);
        }

        private long PrefixSum(int idx) {
            return Query(bit1, idx) * idx - Query(bit2, idx);
        }

        private long RangeSum(int l, int r) {
            return PrefixSum(r) - PrefixSum(l - 1);
        }
    }
}
