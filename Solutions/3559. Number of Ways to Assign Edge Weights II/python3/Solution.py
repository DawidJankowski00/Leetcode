from typing import List

class Solution:
    PRIME_MODULUS = 10**9 + 7

    def fast_exponentiation(self, base: int, exponent: int) -> int:
        result = 1
        base %= self.PRIME_MODULUS

        while exponent > 0:
            if exponent & 1:
                result = (result * base) % self.PRIME_MODULUS

            base = (base * base) % self.PRIME_MODULUS
            exponent >>= 1

        return result

    def compute_tree_properties(self, current_node: int, parent_node: int) -> None:
        self.ancestor_table[current_node][0] = parent_node

        for power in range(1, self.MAX_LOG_STEPS):
            intermediate_node = self.ancestor_table[current_node][power - 1]
            self.ancestor_table[current_node][power] = self.ancestor_table[intermediate_node][power - 1]

        for neighbor in self.graph_adjacency_list[current_node]:
            if neighbor == parent_node:
                continue

            self.node_depth[neighbor] = self.node_depth[current_node] + 1
            self.compute_tree_properties(neighbor, current_node)

    def find_lowest_common_ancestor(self, node_a: int, node_b: int) -> int:
        if self.node_depth[node_a] < self.node_depth[node_b]:
            node_a, node_b = node_b, node_a

        depth_difference = self.node_depth[node_a] - self.node_depth[node_b]

        for power in range(self.MAX_LOG_STEPS - 1, -1, -1):
            if depth_difference & (1 << power):
                node_a = self.ancestor_table[node_a][power]

        if node_a == node_b:
            return node_a

        for power in range(self.MAX_LOG_STEPS - 1, -1, -1):
            if self.ancestor_table[node_a][power] != self.ancestor_table[node_b][power]:
                node_a = self.ancestor_table[node_a][power]
                node_b = self.ancestor_table[node_b][power]

        return self.ancestor_table[node_a][0]

    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        total_nodes = len(edges) + 1

        self.MAX_LOG_STEPS = 1
        while (1 << self.MAX_LOG_STEPS) <= total_nodes:
            self.MAX_LOG_STEPS += 1

        self.graph_adjacency_list = [[] for _ in range(total_nodes + 1)]

        for u, v in edges:
            self.graph_adjacency_list[u].append(v)
            self.graph_adjacency_list[v].append(u)

        self.node_depth = [0] * (total_nodes + 1)
        self.ancestor_table = [[0] * self.MAX_LOG_STEPS for _ in range(total_nodes + 1)]

        self.compute_tree_properties(1, 0)

        query_results = []

        for u, v in queries:
            common_ancestor = self.find_lowest_common_ancestor(u, v)

            path_distance = self.node_depth[u] + self.node_depth[v] - 2 * self.node_depth[common_ancestor]

            if path_distance == 0:
                query_results.append(0)
            else:
                query_results.append(self.fast_exponentiation(2, path_distance - 1))

        return query_results