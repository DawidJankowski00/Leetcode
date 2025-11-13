using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int MinReorder(int n, int[][] connections) {
            
            var adj = new Dictionary<int, List<(int, int)>>();
            for (int i = 0; i < n; i++) {
                adj[i] = new List<(int, int)>();
            }

            foreach (var conn in connections) {
                int u = conn[0];
                int v = conn[1];
                
                adj[u].Add((v, 1));
                adj[v].Add((u, 0));
            }

            int reorders = 0;
            var visited = new HashSet<int> { 0 };
            var queue = new Queue<int>();
            queue.Enqueue(0);

            while (queue.Count > 0) {
                int currentCity = queue.Dequeue();
                
                if (adj.ContainsKey(currentCity)) {
                    foreach (var edge in adj[currentCity]) {
                        int neighbor = edge.Item1;
                        int direction = edge.Item2;
                        
                        if (!visited.Contains(neighbor)) {
                            visited.Add(neighbor);
                            
                            if (direction == 1) {
                                reorders++;
                            }
                            
                            queue.Enqueue(neighbor);
                        }
                    }
                }
            }
            
            return reorders;
        }
    }
}
