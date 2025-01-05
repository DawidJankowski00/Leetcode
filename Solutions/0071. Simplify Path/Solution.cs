using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public string SimplifyPath(string path)
        {
            string[] tmp = path.Split('/');
            Stack<string> stack = new Stack<string>();
            foreach (string v in tmp)
            {
                if (v == "." || v == "")
                {
                    continue;
                }
                if (v == "..")
                {
                    if (stack.Count > 0) stack.Pop();
                }
                else stack.Push(v);
            }
            
            return "/" + string.Join("/", stack.ToArray().Reverse());
        }
    }
}
