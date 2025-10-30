class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vovels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        curr = 0
        n = len(s)
        for v in s[:k]:
            if v in vovels:
                curr += 1
        result = curr

        for i in range(k, n):
            if s[i] in vovels:
                curr += 1
            if s[i-k] in vovels:
                curr -= 1
            if curr > result:
                result = curr
                if result == k:
                    return result
        return result