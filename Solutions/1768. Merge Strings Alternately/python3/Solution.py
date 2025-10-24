class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        state = 0
        if len(word1) > len(word2):
            state = 1
        if len(word1) < len(word2):
            state = 2
        for i in range(min(len(word1), len(word2))):
            result += word1[i]
            result += word2[i]
        if state == 1:
            return result + word1[len(word2):]
        if state == 2:
            return result + word2[len(word1):]
        
        return result