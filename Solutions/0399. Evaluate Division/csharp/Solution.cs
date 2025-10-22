using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public double[] CalcEquation(IList<IList<string>> equations, double[] values, IList<IList<string>> queries) {
            Dictionary<string, Dictionary<string, double>> graph = new Dictionary<string, Dictionary<string, double>>();
            
            for (int i = 0; i < equations.Count; i++)
            {
                string a = equations[i][0];
                string b = equations[i][1];
                double val = values[i];

                if (!graph.ContainsKey(a)) graph[a] = new Dictionary<string, double>();
                if (!graph.ContainsKey(b)) graph[b] = new Dictionary<string, double>();

                graph[a][b] = val;
                graph[b][a] = 1.0 / val;
                
                graph[a][a] = 1.0;
                graph[b][b] = 1.0;
            }

            void dfs(string startNode, string curr, double res, HashSet<string> visited)
            {
                visited.Add(curr);

                graph[startNode][curr] = res;
                graph[curr][startNode] = 1.0 / res;

                foreach (string neighbor in graph[curr].Keys.ToList())
                {
                    if (!visited.Contains(neighbor))
                    {
                        double newRes = res * graph[curr][neighbor];
                        dfs(startNode, neighbor, newRes, visited);
                    }
                }
            }

            foreach (string startNode in graph.Keys.ToList())
            {
                dfs(startNode, startNode, 1.0, new HashSet<string>()); 
            }

            double[] result = new double[queries.Count];
            for (int i = 0; i < queries.Count; i++)
            {
                string a = queries[i][0];
                string b = queries[i][1];

                if (graph.ContainsKey(a) && graph[a].ContainsKey(b))
                {
                    result[i] = graph[a][b];
                }
                else
                {
                    result[i] = -1.0;
                }
            }
            
            return result;
        }
    }
}
