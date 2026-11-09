import heapq
from typing import List

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:

        if not heights or not queries:
            return []

        n = len(heights)
        m = len(queries)
        
        result = [-1] * m
        deferred = [[] for _ in range(n)]
        min_heap = []

        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a  
            if a == b or heights[a] < heights[b]:
                result[i] = b  
            else:
                deferred[b].append((heights[a], i))  

        for i in range(n):

            for height, query_index in deferred[i]:
                heapq.heappush(min_heap, (height, query_index))
            
            
            while min_heap and min_heap[0][0] < heights[i]:
                _, query_index = heapq.heappop(min_heap)
                result[query_index] = i

        return result
