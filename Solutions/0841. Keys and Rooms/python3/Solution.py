from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        to_visit = set()
        to_visit.add(0)
        while len(to_visit) > 0:
            p = to_visit.pop()
            visited.add(p)
            for v in rooms[p]:
                if v not in visited and v not in to_visit:
                    to_visit.add(v)
            to_visit.discard(p)

        return len(visited) == len(rooms)

