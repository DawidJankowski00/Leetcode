using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int TotalNumbers(int[] digits) {
            int result = 0;
            bool[] tmp = new bool[1000];
            int l = digits.Length;
            for (int i = 0; i < l; i++) {
                if (digits[i] == 0) {
                    continue;
                }
                for (int j = 0; j < l; j++) {
                    if (i == j) {
                        continue;
                    }
                    for (int k = 0; k < l; k++) {
                        if (j == k || i == k) {
                            continue;
                        }
                        if (digits[k] % 2 == 0) {
                            int x = digits[i] * 100 + digits[j] * 10 + digits[k];
                            if (!tmp[x]) {
                                tmp[x] = true;
                                result++;
                            }
                        }
                    }
                }
            }
            return result;
        }
    }
}
