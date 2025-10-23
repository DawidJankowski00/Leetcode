from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not self.canFinish(numCourses, prerequisites):
            return []
        graph = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            graph[a].append(b)
        visited = [0] * numCourses
        result = []
        def dfs(v):
            if visited[v] == 1:
                return

            for k in graph[v]:
                dfs(k)
            visited[v] = 1
            result.append(v)
        
        for i in range(numCourses):
            dfs(i)

        return result
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            graph[b].append(a)

        visited = [0] * numCourses

        def dfs(v):
            if visited[v] == 1:
                return True
            if visited[v] == -1:
                return False
            visited[v] = -1

            for k in graph[v]:
                if not dfs(k):
                    return False
            visited[v] = 1
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True