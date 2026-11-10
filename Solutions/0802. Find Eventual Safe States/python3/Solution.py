from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        result = []
        safe = {}
        def visit_node(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for v in graph[i]:
                if not visit_node(v):
                    return False
            safe[i] = True
            return True

        for i in range(len(graph)):
            if visit_node(i):
                result.append(i)

        return result
