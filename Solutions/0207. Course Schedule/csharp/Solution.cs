using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public bool CanFinish(int numCourses, int[][] prerequisites) {
            List<List<int>> graph = new List<List<int>>(numCourses);
            for (int i = 0; i < numCourses; i++) graph.Add(new List<int>());
            
            foreach (int[] prerequisite in prerequisites) graph[prerequisite[1]].Add(prerequisite[0]);
            
            int[] visited = new int[numCourses];

            bool dfs(int v)
            {
                if (visited[v] == 1) return true;
                if (visited[v] == -1) return false;
                visited[v] = -1;
                foreach (int item in graph[v]) if (!dfs(item)) return false;
                visited[v] = 1;
                return true;
            }
            for (int i = 0; i < numCourses; i++) if (!dfs(i)) return false;
            return true;
        }
    }
}
