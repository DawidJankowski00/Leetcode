using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public string ProcessStr(string s) {
            StringBuilder result = new StringBuilder();
            foreach (char c in s) {
                switch (c) {
                    case '*':
                        if (result.Length > 0) {
                            result.Remove(result.Length - 1, 1);
                        }
                        break;
                    case '#':
                        result.Append(result.ToString());
                        break;
                    case '%':
                        ReverseStringBuilder(result);
                        break;
                    default:
                        result.Append(c);
                        break;
                }
            }
            return result.ToString();
        }
        private void ReverseStringBuilder(StringBuilder sb) 
        {
            int left = 0;
            int right = sb.Length - 1;
            while (left < right) {
                char temp = sb[left];
                sb[left] = sb[right];
                sb[right] = temp;
                left++;
                right--;
            }
        }
        
    }
}
