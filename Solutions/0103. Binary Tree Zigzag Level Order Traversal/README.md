# [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)
**Tematy:** `Tree`, `Breadth-First Search`, `Binary Tree`  
**Link:** [https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

---
Given the `root` of a binary tree, return *the zigzag level order traversal of its nodes' values*. (i.e., from left to right, then right to left for the next level and alternate between).

**Example 1:**

![image](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

```text
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
```

**Example 2:**

```text
Input: root = [1]
Output: [[1]]
```

**Example 3:**

```text
Input: root = []
Output: []
```

**Constraints:**

	- The number of nodes in the tree is in the range `[0, 2000]`.

	- `-100 <= Node.val <= 100`
