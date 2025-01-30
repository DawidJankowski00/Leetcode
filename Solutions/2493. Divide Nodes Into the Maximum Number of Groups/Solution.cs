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

public class Solution
{
    public int MagnificentSets(int n, int[][] edges)
    {
        List<int>[] graph = new List<int>[n];
        for (int i = 0; i < n; i++) 
        {
            graph[i] = new List<int>();
        }
        
        foreach (var edge in edges)
        {
            int u = edge[0] - 1;
            int v = edge[1] - 1;
            graph[u].Add(v);
            graph[v].Add(u);
        }

        int[] visited = new int[n];
        List<List<int>> groups = new List<List<int>>();

        for (int i = 0; i < n; i++)
        {
            if (visited[i] == 0)
            {
                Stack<int> stack = new Stack<int>();
                stack.Push(i);
                visited[i] = 1;
                List<int> group = new List<int> { i };

                while (stack.Count > 0)
                {
                    int u = stack.Pop();
                    foreach (int v in graph[u])
                    {
                        if (visited[v] == 0)
                        {
                            visited[v] = visited[u] + 1;
                            stack.Push(v);
                            group.Add(v);
                        }
                        else if ((visited[u] % 2) == (visited[v] % 2))
                        {
                            return -1;
                        }
                    }
                }
                groups.Add(group);
            }
        }

        int BfsMaxDepth(int start)
        {
            int maxDepth = 0;
            HashSet<int> visitedSet = new HashSet<int> { start };
            Queue<int> queue = new Queue<int>();
            queue.Enqueue(start);

            while (queue.Count > 0)
            {
                maxDepth++;
                int size = queue.Count;
                for (int i = 0; i < size; i++)
                {
                    int node = queue.Dequeue();
                    foreach (int neighbor in graph[node])
                    {
                        if (!visitedSet.Contains(neighbor))
                        {
                            visitedSet.Add(neighbor);
                            queue.Enqueue(neighbor);
                        }
                    }
                }
            }
            return maxDepth;
        }

        return groups.Sum(group => group.Max(BfsMaxDepth));
    }
}

}
