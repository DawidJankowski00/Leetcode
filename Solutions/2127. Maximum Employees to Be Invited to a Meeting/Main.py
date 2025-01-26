from collections import deque
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.maximumInvitations([2,2,1,2]))
    print(time.time() - start)

class Solution(object):
    def maximumInvitations(self, favorite):
        n = len(favorite)
        in_degree = [0] * n
        lengths = [0] * n
        processed = [False] * n
        

        for person in favorite:
            in_degree[person] += 1

        queue = deque([i for i in range(n) if in_degree[i] == 0])

        while queue:
            current = queue.popleft()
            processed[current] = True
            next_person = favorite[current]
            lengths[next_person] = max(lengths[next_person], lengths[current] + 1)
            in_degree[next_person] -= 1
            if in_degree[next_person] == 0:
                queue.append(next_person)

        largest_cycle = 0
        combined_pairs = 0

        for index in range(n):
            if not processed[index]:
                cycle_size = 0
                node = index
                while not processed[node]:
                    processed[node] = True
                    node = favorite[node]
                    cycle_size += 1

                if cycle_size == 2:
                    combined_pairs += 2 + lengths[index] + lengths[favorite[index]]
                else:
                    largest_cycle = max(largest_cycle, cycle_size)

        return max(largest_cycle, combined_pairs)

        

if __name__ == '__main__':
    sys.exit(main())