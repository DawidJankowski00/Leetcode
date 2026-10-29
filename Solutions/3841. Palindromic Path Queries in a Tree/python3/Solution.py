class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        node_parent = [0] * n
        node_depth = [0] * n
        bfs_traversal = [0]

        for curr in bfs_traversal:
            for nxt in adj[curr]:
                if nxt != node_parent[curr]:
                    node_parent[nxt] = curr
                    node_depth[nxt] = node_depth[curr] + 1
                    bfs_traversal.append(nxt)

        subtree_sz = [1] * n
        heavy_child = [-1] * n

        for curr in reversed(bfs_traversal[1:]):
            p = node_parent[curr]
            subtree_sz[p] += subtree_sz[curr]
            if heavy_child[p] == -1 or subtree_sz[curr] > subtree_sz[heavy_child[p]]:
                heavy_child[p] = curr

        chain_leader = list(range(n))
        tin = [0] * n
        timer = 1

        dfs_stack = [0]
        while dfs_stack:
            curr = dfs_stack.pop()
            tin[curr] = timer
            timer += 1

            light_nodes = []
            for nxt in adj[curr]:
                if nxt != node_parent[curr] and nxt != heavy_child[curr]:
                    light_nodes.append(nxt)

            for l_node in light_nodes:
                dfs_stack.append(l_node)

            if heavy_child[curr] != -1:
                chain_leader[heavy_child[curr]] = chain_leader[curr]
                dfs_stack.append(heavy_child[curr])

        fenwick_tree = [0] * (n + 2)

        def bit_toggle(idx: int, val: int) -> None:
            while idx <= n:
                fenwick_tree[idx] ^= val
                idx += idx & -idx

        def bit_prefix(idx: int) -> int:
            total = 0
            while idx > 0:
                total ^= fenwick_tree[idx]
                idx -= idx & -idx
            return total

        def query_segment(left: int, right: int) -> int:
            return bit_prefix(right) ^ bit_prefix(left - 1)

        char_masks = [1 << (ord(ch) - 97) for ch in s]
        for node_id in range(n):
            bit_toggle(tin[node_id], char_masks[node_id])

        def compute_path_xor(node_a: int, node_b: int) -> int:
            accumulated = 0
            while chain_leader[node_a] != chain_leader[node_b]:
                if node_depth[chain_leader[node_a]] < node_depth[chain_leader[node_b]]:
                    node_a, node_b = node_b, node_a
                
                accumulated ^= query_segment(tin[chain_leader[node_a]], tin[node_a])
                node_a = node_parent[chain_leader[node_a]]

            if node_depth[node_a] > node_depth[node_b]:
                node_a, node_b = node_b, node_a

            accumulated ^= query_segment(tin[node_a], tin[node_b])
            return accumulated

        results = []
        for raw_query in queries:
            action, *params = raw_query.split()
            if action == "update":
                target_node = int(params[0])
                new_mask = 1 << (ord(params[1]) - 97)
                diff = char_masks[target_node] ^ new_mask
                if diff:
                    char_masks[target_node] = new_mask
                    bit_toggle(tin[target_node], diff)
            else:
                start_node, end_node = int(params[0]), int(params[1])
                path_mask = compute_path_xor(start_node, end_node)
                results.append((path_mask & (path_mask - 1)) == 0)

        return results