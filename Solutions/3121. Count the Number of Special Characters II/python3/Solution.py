class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first_upper = {}
        last_lower = {}
        result = 0
        
        for i, v in enumerate(word):
            if v.islower():
                last_lower[v] = i
            else:
                if v.lower() not in first_upper:
                    first_upper[v.lower()] = i
        for v in last_lower:
            if v in first_upper and last_lower[v] < first_upper[v]:
                result += 1

        return result

