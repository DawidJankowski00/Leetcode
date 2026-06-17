using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{

    public class Solution {
        public char ProcessStr(string s, long k) {
            long targetLength = CalculateFinalLength(s);

            if (k >= targetLength) {
                return '.';
            }

            return FindCharAtIndex(s, k, targetLength);
        }

        private long CalculateFinalLength(string s) {
            long targetLength = 0;
            foreach (char character in s) {
                if (character == '*') {
                    targetLength = Math.Max(targetLength - 1, 0);
                } 
                else if (character == '#') {
                    targetLength *= 2;
                } 
                else if (character != '%') {
                    targetLength++;
                }
            }
            return targetLength;
        }

        private char FindCharAtIndex(string s, long k, long targetLength) {
            int strLength = s.Length;

            for (int i = strLength - 1; i >= 0; i--) {
                char character = s[i];
                if (character == '*') {
                    targetLength++;
                } 
                else if (character == '#') {
                    long halfLength = targetLength / 2;
                    if (k >= halfLength) {
                        k -= halfLength;
                    }
                    targetLength /= 2;
                } 
                else if (character == '%') {
                    k = targetLength - 1 - k;
                } 
                else {
                    if (targetLength == k + 1) {
                        return character;
                    }
                    targetLength--;
                }
            }

            return '.';
        }
    }
}
