using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int[] FindRedundantConnection(int[][] edges)
        {
            var graph = new Dictionary<int, List<int>>();

            bool dfs(int node, int target, HashSet<int> visited)
            {
                if (node == target)
                    return true;
                visited.Add(node);
                foreach (var n in graph[node])
                {
                    if (!visited.Contains(n))
                    {
                        if (dfs(n, target, visited))
                            return true;
                    }
                }
                return false;
            }

            foreach (var edge in edges)
            {
                int a = edge[0];
                int b = edge[1];
                HashSet<int> visited = new HashSet<int>();
                if (graph.ContainsKey(a) && graph.ContainsKey(b) && dfs(a,b,visited))
                    return edge;
                if (!graph.ContainsKey(a))
                    graph[a] = new List<int>();
                if (!graph.ContainsKey(b))
                    graph[b] = new List<int>();
                graph[a].Add(b);
                graph[b].Add(a);
            }
            return [];
        }
    }
}
