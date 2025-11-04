using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public string RemoveStars(string s) {
            Stack<char> stack = new Stack<char>();

            foreach (char v in s)
            {
                if (v == '*') stack.Pop();
                else stack.Push(v);
            }
            char[] resultArray = stack.ToArray();
            Array.Reverse(resultArray);
            return new string(resultArray);
        }
    }
}
