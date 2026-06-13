using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public string MapWordWeights(string[] words, int[] weights) {
            StringBuilder result = new StringBuilder();
            int asciiA = 'a';
            int asciiZ = 'z';

            foreach (string word in words) 
            {
                int tmp = 0;
                foreach (char v in word) 
                {
                    tmp += weights[v - asciiA];
                }

                tmp %= 26;
                
                char mappedChar = (char)(asciiZ - tmp);
                result.Append(mappedChar);
            }

            return result.ToString();
        }
    }
}
