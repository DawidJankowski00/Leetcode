# [1408. String Matching in an Array](https://leetcode.com/problems/string-matching-in-an-array/)

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
**Tematy:** `Array`, `String`, `String Matching`  
**Link:** [https://leetcode.com/problems/string-matching-in-an-array/](https://leetcode.com/problems/string-matching-in-an-array/)

---
Given an array of string `words`, return all strings in* *`words`* *that are a substring of another word. You can return the answer in **any order**.

**Example 1:**

```text
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
```

**Example 2:**

```text
Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".
```

**Example 3:**

```text
Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.
```

**Constraints:**

	- `1 <= words.length <= 100`

	- `1 <= words[i].length <= 30`

	- `words[i]` contains only lowercase English letters.

	- All the strings of `words` are **unique**.
