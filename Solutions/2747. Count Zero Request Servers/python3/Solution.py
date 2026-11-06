class Solution:
    def countServers(
        self, n: int, logs: List[List[int]], x: int, queries: List[int]
    ) -> List[int]:
        events = sorted(logs, key=lambda item: item[1])
        total_events = len(events)

        sorted_q = sorted(range(len(queries)), key=lambda idx: queries[idx])

        server_hits = [0] * (n + 1)
        unique_active = 0
        w_start = 0
        w_end = 0

        res = [0] * len(queries)

        for q_idx in sorted_q:
            t_end = queries[q_idx]
            t_start = t_end - x

        while w_end < total_events and events[w_end][1] <= t_end:
            s_id = events[w_end][0]
            unique_active += 1 if server_hits[s_id] == 0 else 0
            server_hits[s_id] += 1
            w_end += 1

        while w_start < w_end and events[w_start][1] < t_start:
            s_id = events[w_start][0]
            server_hits[s_id] -= 1
            if not server_hits[s_id]:
                unique_active -= 1
                w_start += 1

        res[q_idx] = n - unique_active

        return res