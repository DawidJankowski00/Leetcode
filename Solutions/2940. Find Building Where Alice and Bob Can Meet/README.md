# [2940. Find Building Where Alice and Bob Can Meet](https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/)

![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)
**Tematy:** `Array`, `Binary Search`, `Stack`, `Binary Indexed Tree`, `Segment Tree`, `Heap (Priority Queue)`, `Monotonic Stack`  
**Link:** [https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/](https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/)

---
You are given a **0-indexed** array `heights` of positive integers, where `heights[i]` represents the height of the `i^th` building.

If a person is in building `i`, they can move to any other building `j` if and only if `i < j` and `heights[i] < heights[j]`.

You are also given another array `queries` where `queries[i] = [a_i, b_i]`. On the `i^th` query, Alice is in building `a_i` while Bob is in building `b_i`.

Return *an array* `ans` *where* `ans[i]` *is **the index of the leftmost building** where Alice and Bob can meet on the* `i^th` *query*. *If Alice and Bob cannot move to a common building on query* `i`, *set* `ans[i]` *to* `-1`.

**Example 1:**

```text
Input: heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
Output: [2,5,-1,5,2]
Explanation: In the first query, Alice and Bob can move to building 2 since heights[0] **Example 2:**

```text
Input: heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]
Output: [7,6,-1,4,6]
Explanation: In the first query, Alice can directly move to Bob's building since heights[0]

**Constraints:**

	- `1 <= heights.length <= 5 * 10^4`

	- `1 <= heights[i] <= 10^9`

	- `1 <= queries.length <= 5 * 10^4`

	- `queries[i] = [a_i, b_i]`

	- `0 <= a_i, b_i <= heights.length - 1`
