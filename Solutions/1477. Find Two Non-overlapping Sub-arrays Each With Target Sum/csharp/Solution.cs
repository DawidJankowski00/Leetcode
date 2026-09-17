using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int MinSumOfLengths(int[] arr, int target) {
            int n = arr.Length;
            int[] min_lens = new int[n];
            int ans = int.MaxValue;
            int curr = 0;
            int l = 0;
            int min_len = int.MaxValue;

            for (int r = 0; r < n; r++) {
                curr += arr[r];

                while (curr > target) {
                    curr -= arr[l];
                    l++;
                }

                if (curr == target) {
                    int length = r - l + 1;
                    if (l > 0 && min_lens[l - 1] != int.MaxValue) {
                        ans = Math.Min(ans, length + min_lens[l - 1]);
                    }

                    min_len = Math.Min(min_len, length);
                }
                min_lens[r] = min_len;
            }

            return ans != int.MaxValue ? ans : -1;
        }
    }
}
