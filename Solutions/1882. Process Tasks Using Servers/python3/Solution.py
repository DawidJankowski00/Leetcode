from heapq import heapify, heappop, heappush


class Solution:

    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = [(weight, idx) for idx, weight in enumerate(servers)]
        heapify(available)

        occupied = []
        res = []

        for arrival, duration in enumerate(tasks):
            while occupied and occupied[0][0] <= arrival:
                _, s_weight, s_idx = heappop(occupied)
                heappush(available, (s_weight, s_idx))

        if available:
            s_weight, s_idx = heappop(available)
            release_time = arrival + duration
        else:
            finish, s_weight, s_idx = heappop(occupied)
            release_time = finish + duration

        heappush(occupied, (release_time, s_weight, s_idx))
        res.append(s_idx)

        return res