from collections import defaultdict
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.mostProfitablePath([[0,1],[1,2],[1,3],[3,4]], 3, [-2,4,2,-4,6]))
    print(time.time() - start)

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        bob_time = {}  
        path_to_root = {}  

        def find_bob_path(node, parent, time):
            if node == 0:
                bob_time[node] = time
                return True
            for neighbor in tree[node]:
                if neighbor != parent and find_bob_path(neighbor, node, time + 1):
                    bob_time[node] = time
                    path_to_root[node] = parent
                    return True
            return False

        find_bob_path(bob, -1, 0)

        def dfs_alice(node, parent, time):
            is_leaf = True
            max_profit = float('-inf')


            if node in bob_time:
                if bob_time[node] > time:
                    net_amount = amount[node]  
                elif bob_time[node] == time:
                    net_amount = amount[node] // 2  
                else:
                    net_amount = 0  
            else:
                net_amount = amount[node]

            for neighbor in tree[node]:
                if neighbor != parent:
                    is_leaf = False
                    max_profit = max(max_profit, dfs_alice(neighbor, node, time + 1))

            return net_amount if is_leaf else net_amount + max_profit

        return dfs_alice(0, -1, 0)



if __name__ == '__main__':
    sys.exit(main())