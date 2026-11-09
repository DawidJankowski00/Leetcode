import heapq

class Solution:
    def busiestServers(self, k, arrival, load):
        available_pool = list(range(k))
        running_tasks = []
        handled_counts = [0] * k

        for req_idx, start_time in enumerate(arrival):
            task_duration = load[req_idx]

            while running_tasks and running_tasks[0][0] <= start_time:
                _, server_id = heapq.heappop(running_tasks)
                virtual_index = req_idx + (server_id - req_idx) % k
                heapq.heappush(available_pool, virtual_index)

            if not available_pool:
                continue

            chosen_server = heapq.heappop(available_pool) % k
            handled_counts[chosen_server] += 1

            finish_time = start_time + task_duration
            heapq.heappush(running_tasks, (finish_time, chosen_server))

        peak_traffic = max(handled_counts)
        return [srv for srv, count in enumerate(handled_counts) if count == peak_traffic]