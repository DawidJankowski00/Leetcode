using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public IList<int> EventualSafeNodes(int[][] graph)
        {
            int n = graph.Length;
            List<int> result = new List<int>();
            Dictionary<int, bool> safe = new Dictionary<int, bool>();

            bool visit_node(int i)
            {
                if (safe.ContainsKey(i))
                    return safe[i];
                safe[i] = false;
                foreach(int v in graph[i])
                {
                    if (!visit_node(v))
                    {
                        return false;
                    }
                }
                safe[i] = true;
                return true;
            }

            for (int i = 0; i < n; i++)
            {
                if (visit_node(i))
                    result.Add(i);
            }
            return result;
        }
    }
}
