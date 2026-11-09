using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    using System;
    using System.Collections.Generic;
    using System.Linq;
    
    using System;
    using System.Collections.Generic;
    using System.Linq;

    public class Solution
    {
        public int MagnificentSets(int n, int[][] edges)
        {
            List<int>[] graph = Enumerable.Repeat(0, n).Select(_ => new List<int>()).ToArray();

            foreach (var edge in edges)
            {
                int u = edge[0] - 1, v = edge[1] - 1;
                graph[u].Add(v);
                graph[v].Add(u);
            }

            int[] visited = new int[n];
            List<List<int>> groups = new();

            for (int i = 0; i < n; i++)
            {
                if (visited[i] == 0)
                {
                    if (!IsBipartite(i, graph, visited, out List<int> group)) return -1;
                    groups.Add(group);
                }
            }

            return groups.Sum(group => GetMaxBfsDepth(group, graph));
        }

        private bool IsBipartite(int start, List<int>[] graph, int[] visited, out List<int> group)
        {
            Queue<int> queue = new();
            queue.Enqueue(start);
            visited[start] = 1;
            group = new() { start };

            while (queue.Count > 0)
            {
                int u = queue.Dequeue();
                foreach (int v in graph[u])
                {
                    if (visited[v] == 0)
                    {
                        visited[v] = visited[u] + 1;
                        queue.Enqueue(v);
                        group.Add(v);
                    }
                    else if ((visited[u] % 2) == (visited[v] % 2))
                    {
                        return false;
                    }
                }
            }
            return true;
        }

        private int GetMaxBfsDepth(List<int> group, List<int>[] graph)
        {
            int maxDepth = 0;
            foreach (int node in group)
            {
                maxDepth = Math.Max(maxDepth, BfsDepth(node, graph));
            }
            return maxDepth;
        }

        private int BfsDepth(int start, List<int>[] graph)
        {
            int[] level = new int[graph.Length];
            Queue<int> queue = new();
            queue.Enqueue(start);
            level[start] = 1;
            int maxDepth = 0;

            while (queue.Count > 0)
            {
                int u = queue.Dequeue();
                maxDepth = Math.Max(maxDepth, level[u]);

                foreach (int v in graph[u])
                {
                    if (level[v] == 0)
                    {
                        level[v] = level[u] + 1;
                        queue.Enqueue(v);
                    }
                }
            }
            return maxDepth;
        }
    }
}
