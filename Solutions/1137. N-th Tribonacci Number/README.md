# [1137. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/)

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
**Tematy:** `Math`, `Dynamic Programming`, `Memoization`  
**Link:** [https://leetcode.com/problems/n-th-tribonacci-number/](https://leetcode.com/problems/n-th-tribonacci-number/)

---
The Tribonacci sequence T_n is defined as follows:

T_0 = 0, T_1 = 1, T_2 = 1, and T_n+3 = T_n + T_n+1 + T_n+2 for n >= 0.

Given `n`, return the value of T_n.

**Example 1:**

```text
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
```

**Example 2:**

```text
Input: n = 25
Output: 1389537
```

**Constraints:**

	- `0 <= n <= 37`

	- The answer is guaranteed to fit within a 32-bit integer, ie. `answer <= 2^31 - 1`.
